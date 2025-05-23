from django.shortcuts import render,redirect
from account.forms import BusinessContactForm
from django.contrib import messages
from django.apps import apps
from google.protobuf.empty_pb2 import Empty
from django.core.paginator import Paginator
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
        request.session['auth_token'] = response.access_token
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
        merchant_list = list(response.merchants)  # Convert to list for pagination
        
        # Pagination
        paginator = Paginator(merchant_list, 10)  # Show 10 merchants per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'merchant/merchant.html', {
            'merchants': page_obj
        })
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, "Failed to load merchants")
        return render(request, 'merchant/merchant.html', {'merchants': []})

def merchant_detail(request, merchant_id):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    metadata = [('authorization', f"Bearer {request.session['auth_token']}")]
    
    try:
        # Get merchant details
        merchant_response = invoice_stub.GetMerchant(invoice_pb2.GetMerchantRequest(id=merchant_id), metadata=metadata)
      
        # Initialize variables
        user = None
        error = None
        phone_search = request.GET.get('phone', '').strip()
        
        if phone_search:
            try:
                # Use GetUserByMobile from your proto file
                user = auth_stub.GetUserByMobile(
                    auth_pb2.GetUserByMobileRequest(mobile=phone_search),
                    metadata=metadata
                )
            except grpc.RpcError as e:
                error = f"Error searching user: {e.details()}"
                
        if request.method == 'POST' and 'add_user' in request.POST:
            try:
                create_request = invoice_pb2.CreateMerchantUserRequest(
                    merchant_user=common_pb2.MerchantUser(
                        merchant_id=merchant_id,
                        user_id=int(request.POST.get('user_id')),
                    )
                )
                print("POST data:", request.POST)  
                print("Creating merchant user:", create_request)  
                invoice_stub.CreateMerchantUser(create_request, metadata=metadata)
                messages.success(request, 'User added successfully!')
                return redirect('merchant_detail', merchant_id=merchant_id)
            except grpc.RpcError as e:
                messages.error(request, f"Failed to add user: {e.details()}")
         # Get current merchant users
        merchant_users_response = invoice_stub.ListMerchantUsers(
            invoice_pb2.ListMerchantUsersRequest(merchant_id=merchant_id),
            metadata=metadata
        )
        # Get user details for each merchant user
        merchant_users_data = []
        for mu in merchant_users_response.merchant_users:
            try:
                # Get user details from auth service
                user_response = auth_stub.GetUser(
                    auth_pb2.GetUserRequest(user_id=mu.user_id),
                    metadata=metadata
                )
                merchant_users_data.append({
                    'merchant_user_id': mu.id,  # From MerchantUser
                    'merchant_id': mu.merchant_id,  # From MerchantUser
                    'user_id': mu.user_id,  # From MerchantUser
                    'first_name': user_response.first_name,
                    'last_name': user_response.last_name,
                    'mobile': user_response.mobile,
                    'is_verified': user_response.is_verified,
                    'is_admin': user_response.is_admin,
                    'is_super_user': user_response.is_super_user
                })
            except grpc.RpcError as e:
                merchant_users_data.append({
                    'merchant_user_id': mu.id,
                    'merchant_id': mu.merchant_id,
                    'user_id': mu.user_id,
                    'first_name': 'Unknown',
                    'last_name': 'User',
                    'mobile': 'N/A',
                    'is_admin': False,
                    'is_super_user': False
                })
        page_number = request.GET.get('page', 1)
        paginator = Paginator(merchant_users_data, 3)  # Show 10 users per page
        page_obj = paginator.get_page(page_number)
        context = {
            'merchant': merchant_response.merchant,
            'merchant_users': page_obj,
            'searched_user': user,
            'phone_search': phone_search,
            'error': error
        }
        return render(request, 'merchant/merchant_detail.html', context)
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load merchant details: {e.details()}")
        return redirect('dashboard')


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
    user_response = auth_stub.ListUsers(Empty())
    user_list = list(user_response.users)
    
    page_number = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)  # Show 10 users per page
    page_obj = paginator.get_page(page_number)
    context = {
        'users': page_obj  
    }
    return render(request, 'merchant/user_management.html', context)

def edit_user_management(request, pk):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    
    try:
        # Get the user details
        user = auth_stub.GetUser(
            auth_pb2.GetUserRequest(user_id=pk),
            metadata=metadata
        )
        
        if request.method == 'POST':
            try:
                # Create update request
                update_request = auth_pb2.UpdateUserRequest(
                    user_id=pk,
                    first_name=request.POST.get('first_name', user.first_name),
                    last_name=request.POST.get('last_name', user.last_name),
                    is_admin=request.POST.get('is_admin') == 'on',
                    is_super_user=request.POST.get('is_super_user') == 'on'
                )
                
                # Call the gRPC service to update user
                updated_user = auth_stub.UpdateUser(update_request, metadata=metadata)
                messages.success(request, 'User updated successfully!')
                return redirect('user_management')
                
            except grpc.RpcError as e:
                messages.error(request, f"Failed to update user: {e.details()}")
        
        context = {
            'user': user,
            'pk': pk
        }
        return render(request, 'merchant/edit_user_management.html', context)
        
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load user details: {e.details()}")
        return redirect('user_management')

def delete_user_management(request, pk):
    if request.method == 'POST':
        delete_request = auth_stub.DeleteUserRequest(id=pk)
        auth_stub.DeleteUser(delete_request)
        return redirect('user_management')

def provider(request):
    return render(request, 'merchant/provider.html')


# print(invoice_pb2.CreateMerchantRequest.DESCRIPTOR.fields_by_name.keys())