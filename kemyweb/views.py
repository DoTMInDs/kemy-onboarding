from django.shortcuts import render,redirect
from account.forms import BusinessContactForm
from django.contrib import messages
from django.apps import apps
from google.protobuf.empty_pb2 import Empty
from v1.auth import auth_pb2_grpc,auth_pb2
from v1.invoice import invoice_pb2_grpc,invoice_pb2,common_pb2
import grpc
from django.core.files.storage import default_storage
from django.conf import settings
import os
import uuid

auth_channel = apps.get_app_config('kemyweb').auth_channel
auth_stub=auth_pb2_grpc.AuthStub(auth_channel)

invoice_channel = apps.get_app_config('kemyweb').invoice_channel
invoice_stub=invoice_pb2_grpc.InvoiceServiceStub(invoice_channel)

def refresh_token(request):
    refresh_token = request.session.get('refresh_token')
    if not refresh_token:
        return False
    
    try:
        response = auth_stub.GetNewAccessToken(
            auth_pb2.GetNewAccessTokenRequest(refresh_token=refresh_token)
        )
        request.session['access_token'] = response.access_token
        return True
    except grpc.RpcError:
        return False

# Create your views here.
def home(request):
    form = BusinessContactForm()
    if request.method == 'POST':
        form = BusinessContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has bbeen save successfully!!!')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            
    form = BusinessContactForm()
    context = {
        'form':form
    }
    return render(request, 'site/home.html',context)

def invoice(request):
    return render(request, 'site/invoice.html')

def education(request):
    return render(request, 'site/education.html')

def healthcare(request):
    return render(request, 'site/healthcare.html')

def dashboard(request):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    merchants_response = invoice_stub.ListMerchants(Empty(), metadata=metadata)
    all_merchants = merchants_response.merchants
    first_5_merchants = all_merchants[:5] 
    
    users_response = auth_stub.ListUsers(Empty(), metadata=metadata)
    users_count = len(users_response.users)
    context = {
        'merchants': first_5_merchants,
        'merchants_count': len(all_merchants),
        'users_count': users_count
    }
    return render(request, 'merchant/dashboard.html',context)

def merchant(request):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    try:
        metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
        if request.method == 'POST':
            # Create merchant request with correct field names from proto
            update_request = invoice_pb2.CreateMerchantRequest(
                merchant = common_pb2.Merchant(
                    name=request.POST.get('name'),
                    address=request.POST.get('address'),
                    contact_info=request.POST.get('contact_info'),
                    category=common_pb2.Category.Value(request.POST.get('category').upper())
                )
            )
            # Handle file upload if exists
            if 'logo' in request.FILES:
                logo_file = request.FILES['logo']
                # Generate unique filename
                file_ext = os.path.splitext(logo_file.name)[1]
                filename = f"merchant_logos/{uuid.uuid4()}{file_ext}"
                # Save file to storage
                file_path = default_storage.save(filename, logo_file)
                # Get URL (this depends on your storage backend)
                if hasattr(default_storage, 'url'):
                    logo_url = default_storage.url(file_path)
                else:
                    # For local development
                    logo_url = f"{settings.MEDIA_URL}{file_path}"
                merchant.logo_url = logo_url
            try:
                # Call gRPC service to create merchant
                response = invoice_stub.CreateMerchant(update_request, metadata=metadata)
                messages.success(request, 'Merchant created successfully!')
                return redirect('merchant')
            except grpc.RpcError as e:
                messages.error(request, f"Failed to create merchant: {e.details()}")
        
        # Get list of merchants
        response = invoice_stub.ListMerchants(Empty(), metadata=metadata)
        return render(request, 'merchant/merchant.html', {
            'merchants': response.merchants
        })
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, "Failed to load merchants")
        return render(request, 'merchant/merchant.html', {'merchants': []})

def edit_merchant(request, merchant_id):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    try:
        metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
        if request.method == 'POST':
            update_request = invoice_pb2.UpdateMerchantRequest(
                merchant=common_pb2.Merchant(
                    id=merchant_id,
                    name=request.POST.get('name'),
                    address=request.POST.get('address'),
                    contact_info=request.POST.get('contact_info'),
                    category=common_pb2.Category.Value(request.POST.get('category').upper())
                )
            )
            response = invoice_stub.UpdateMerchant(update_request, metadata=metadata)
            messages.success(request, 'Merchant updated successfully!')
            return redirect('merchant')
        categories = {
            'SCHOOL': 'School',
            'HOTEL': 'Hotel',
            'GENERAL': 'General'
        }
        # Get merchant details for editing
        get_request = invoice_pb2.GetMerchantRequest(id=merchant_id)
        merchant = invoice_stub.GetMerchant(get_request, metadata=metadata)
        context = {
            'merchant': merchant,
            'categories': categories,
            'selected_category': common_pb2.Category.Name(merchant.category)
        }
        return render(request, 'merchant/edit_merchant.html', context)
        
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to edit merchant: {e.details()}")
        return redirect('merchant')
    
def delete_merchant(request, merchant_id):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    
    try:
        metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
        
        if request.method == 'POST':
            # Create delete request
            delete_request = invoice_pb2.DeleteMerchantRequest(id=merchant_id)
            
            # Call gRPC service to delete merchant
            invoice_stub.DeleteMerchant(delete_request, metadata=metadata)
            messages.success(request, 'Merchant deleted successfully!')
            return redirect('merchant')
        
        # If not POST, show confirmation page
        get_request = invoice_pb2.GetMerchantRequest(id=merchant_id)
        merchant = invoice_stub.GetMerchant(get_request, metadata=metadata)
        return render(request, 'merchant/delete_merchant.html', {'merchant': merchant})
        
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to delete merchant: {e.details()}")
        return redirect('merchant')  

def merchant_provider(request):
    return render(request, 'merchant/merchant_provider.html')

def merchant_account(request):
    return render(request, 'merchant/merchant_account.html')

def user_management(request):
    response = auth_stub.ListUsers(Empty())
    context = {
        'users': response.users  
    }
    return render(request, 'merchant/user_management.html', context)

def edit_user_management(request, pk):
    if request.method == 'POST':
        response = auth_stub.ListUsers(Empty(),pk=pk)
        if response.is_valid():
            response.save()
            return redirect('user_management')
    context = {
        'users': response.users
    }
    return render(request, 'merchant/edit_user_management.html',context)

def delete_user_management(request, pk):
    if request.method == 'POST':
        delete_request = auth_stub.DeleteUserRequest(id=pk)
        auth_stub.DeleteUser(delete_request)
        return redirect('user_management')

def provider(request):
    return render(request, 'merchant/provider.html')


# print(invoice_pb2.CreateMerchantRequest.DESCRIPTOR.fields_by_name.keys())