from django.shortcuts import render,redirect
from django.contrib import messages
from django.apps import apps
from google.protobuf.empty_pb2 import Empty
from django.core.paginator import Paginator
from v1.auth import auth_pb2_grpc,auth_pb2
from v1.invoice import invoice_pb2_grpc,invoice_pb2,common_pb2 as invoice_common
from v1.payment import payment_pb2, payment_pb2_grpc,common_pb2 as payment_common
import grpc
from django.core.files.storage import default_storage
from django.conf import settings
import os
import uuid

# Create your views here.
auth_channel = apps.get_app_config('kemyapp').auth_channel
auth_stub=auth_pb2_grpc.AuthStub(auth_channel)

invoice_channel = apps.get_app_config('kemyapp').invoice_channel
invoice_stub=invoice_pb2_grpc.InvoiceServiceStub(invoice_channel)

payment_channel = apps.get_app_config('kemyapp').payment_channel
payment_stub = payment_pb2_grpc.PaymentServiceStub(payment_channel)

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

def login_view(request):
    if request.method == 'POST':
        try:
            # Call auth service
            login_request = auth_pb2.LoginRequest(
                mobile=request.POST['mobile'],
                pin=request.POST['pin']
            )
            response = auth_stub.LoginUser(login_request)
            
            # Store tokens in session
            request.session['auth_token'] = response.access_token
            request.session['refresh_token'] = response.refresh_token
            request.session['access_token'] = response.access_token
            
            # Verify session is saved
            print("Token stored:", request.session.get('auth_token'))  # Debug print
            
            # Redirect to merchant page
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
            
        except Exception as e:
            print('login failed')
            messages.error(request, f"Login failed: {str(e)}")
            return render(request, 'account/login.html')
    return render(request, 'account/login.html')

def logout_view(request):
    request.session.flush()  # This clears all session data
    return redirect('login')

def dashboard(request):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    merchants_response = invoice_stub.ListMerchants(Empty(), metadata=metadata)
    all_merchants = merchants_response.merchants
    first_5_merchants = all_merchants[:5] 
    
    # users_response = auth_stub.ListUsers(Empty(), metadata=metadata)
    # users_count = len(users_response.users)
    total_users = 0
    page_token = ""
    while True:
        user_request = auth_pb2.ListUsersRequest(page_size=100, page_token=page_token)
        user_response = auth_stub.ListUsers(user_request, metadata=metadata)
        total_users += len(user_response.users)

        if not user_response.next_page_token:
            break
        page_token = user_response.next_page_token
    context = {
        'merchants': first_5_merchants,
        'merchants_count': len(all_merchants),
        'users_count': total_users
    }
    return render(request, 'merchant/dashboard.html',context)

def merchant(request):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    try:
        metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
        search_query = request.GET.get('search', '').strip()
        # Get list of merchants
        # Convert to list for pagination
        response = invoice_stub.ListMerchants(Empty(), metadata=metadata)
        merchant_list = list(response.merchants) 
        
        if search_query:
            try:
                # Try searching by ID first
                try:
                    merchant_id = int(search_query)
                    merchant = invoice_stub.GetMerchant(
                        invoice_pb2.GetMerchantRequest(id=merchant_id),
                        metadata=metadata
                    )
                    merchant_list = [merchant.merchant]
                except ValueError:
                    # If not a number, search by name or contact info
                    merchant_list = [
                        m for m in merchant_list 
                        if (search_query.lower() in m.name.lower()) or 
                           (search_query in m.contact_info)
                    ]
            except grpc.RpcError as e:
                if e.code() == grpc.StatusCode.NOT_FOUND:
                    messages.info(request, "No merchant found with that ID")
                else:
                    messages.error(request, f"Search error: {e.details()}")
                merchant_list = []
        
        
        if request.method == 'POST':
            # Create merchant request with correct field names from proto
            update_request = invoice_pb2.CreateMerchantRequest(
                merchant = invoice_common.Merchant(
                    name=request.POST.get('name'),
                    address=request.POST.get('address'),
                    contact_info=request.POST.get('contact_info'),
                    category=invoice_common.Category.Value(request.POST.get('category').upper())
                )
            )
            if 'logo' in request.FILES:
                    logo_file = request.FILES['logo']
                    file_ext = os.path.splitext(logo_file.name)[1]
                    filename = f"merchant_logos/{uuid.uuid4()}{file_ext}"
                    file_path = default_storage.save(filename, logo_file)
                    logo_url = default_storage.url(file_path) if hasattr(default_storage, 'url') else f"{settings.MEDIA_URL}{file_path}"
                    update_request.merchant.logo_url = logo_url
            try:
                # Call gRPC service to create merchant
                response = invoice_stub.CreateMerchant(update_request, metadata=metadata)
                messages.success(request, 'Merchant created successfully!')
                return redirect('merchant')
            except grpc.RpcError as e:
                messages.error(request, f"Failed to create merchant: {e.details()}")
        
        # Pagination
        paginator = Paginator(merchant_list, 8)  # Show 8 merchants per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'merchant/merchant.html', {
            'merchants': page_obj,
            'search_query': search_query,
            'id_search': search_query,
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
                    merchant_user=invoice_common.MerchantUser(
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
                merchant=invoice_common.Merchant(
                    id=merchant_id,
                    name=request.POST.get('name'),
                    address=request.POST.get('address'),
                    contact_info=request.POST.get('contact_info'),
                    category=invoice_common.Category.Value(request.POST.get('category').upper())
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
            'selected_category': invoice_common.Category.Name(merchant.category)
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
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    
    try:
        search_query = request.GET.get('search', '').strip()
        # Handle provider creation
        if request.method == 'POST':
            try:
                provider_request = payment_common.MerchantProviderAccount(
                    merchant_id=int(request.POST.get('merchant_id')),
                    provider_id=request.POST.get('provider_id'),
                    api_id=request.POST.get('api_id'),
                    api_key=request.POST.get('api_key'),
                    api_url=request.POST.get('api_url')
                )
                payment_stub.AddProviderAccountToMerchant(provider_request, metadata=metadata)
                messages.success(request, 'Merchant provider added successfully!')
                return redirect('merchant_provider')
            except grpc.RpcError as e:
                messages.error(request, f"Failed to add merchant provider: {e.details()}")
        
        # Get list of merchants for the dropdown
        merchants_response = invoice_stub.ListMerchants(Empty(), metadata=metadata)
        merchants = list(merchants_response.merchants)
        
        # Get list of available providers
        providers_response = payment_stub.ListProviders(
            payment_pb2.ListProvidersRequest(active_only=True),
            metadata=metadata
        )
        available_providers = list(providers_response.providers)
        
        # Get merchant-provider accounts for each merchant
        merchant_providers = []
        for merchant in merchants:
            try:
                accounts_response = payment_stub.GetMerchantProviderAccounts(
                    payment_pb2.GetMerchantProviderAccountsRequest(merchant_id=merchant.id),
                    metadata=metadata
                )
                accounts = list(accounts_response.accounts)
                
                # Apply search filter if query exists
                if search_query:
                    accounts = [
                        acc for acc in accounts
                        if (search_query.lower() in str(merchant.id)) or
                           (search_query.lower() in merchant.name.lower()) or
                           (search_query.lower() in acc.provider_id.lower())
                    ]
                
                merchant_providers.extend(accounts)
            except grpc.RpcError as e:
                messages.warning(request, f"Could not load providers for merchant {merchant.id}: {e.details()}")
                continue
        paginator = Paginator(merchant_providers, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'merchants': merchants,
            'available_providers': available_providers,
            'merchant_providers': page_obj,
            'search_query': search_query
        }
        return render(request, 'merchant/merchant_provider.html', context)
        
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load merchant providers: {e.details()}")
        return render(request, 'merchant/merchant_provider.html', {
            'merchants': [],
            'available_providers': [],
            'merchant_providers': []
        })

def edit_merchant_provider(request, merchant_id):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    
    try:
        if request.method == 'POST':
            try:
                update_request = payment_common.MerchantProviderAccount(
                    merchant_id=merchant_id,
                    provider_id=request.POST.get('provider_id'),
                    api_id=request.POST.get('api_id'),
                    api_key=request.POST.get('api_key'),
                    api_url=request.POST.get('api_url')
                )
                payment_stub.UpdateMerchantProviderAccount(update_request, metadata=metadata)
                messages.success(request, 'Merchant provider updated successfully!')
                return redirect('merchant_provider')
            except grpc.RpcError as e:
                messages.error(request, f"Failed to update merchant provider: {e.details()}")
                return redirect('merchant_provider')
        
        # Get merchant details
        merchant = invoice_stub.GetMerchant(
            invoice_pb2.GetMerchantRequest(id=merchant_id),
            metadata=metadata
        )
        
        # Get provider details
        provider_accounts = payment_stub.GetMerchantProviderAccounts(
            payment_pb2.GetMerchantProviderAccountsRequest(merchant_id=merchant_id),
            metadata=metadata
        )
        
        # Get available providers
        providers_response = payment_stub.ListProviders(
            payment_pb2.ListProvidersRequest(active_only=True),
            metadata=metadata
        )
        
        context = {
            'merchant': merchant,
            'provider': provider_accounts.accounts[0],  # Assuming one provider per merchant
            'available_providers': providers_response.providers
        }
        return render(request, 'merchant/edit_merchant_provider.html', context)
        
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load merchant provider details: {e.details()}")
        return redirect('merchant_provider')
        
def merchant_account(request):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    
    try:
        # Handle account creation
        if request.method == 'POST':
            try:
                # Create merchant account request
                account_request = payment_common.MerchantAccount(
                    merchant_id=int(request.POST.get('merchant_id')),
                    bank_name=request.POST.get('bank_name', ''),
                    bank_account_name=request.POST.get('bank_account_name', ''),
                    bank_branch_name=request.POST.get('bank_branch_name', ''),
                    bank_branch_code=request.POST.get('bank_branch_code', ''),
                    bank_account_number=request.POST.get('bank_account_number', ''),
                    bank_routing_number=request.POST.get('bank_routing_number', ''),
                    account_currency=request.POST.get('account_currency', 'USD'),
                    is_active=request.POST.get('is_active', 'false').lower() == 'true'
                )
                
                # Call the gRPC service to create account
                payment_stub.OnboardMerchant(account_request, metadata=metadata)
                messages.success(request, 'Merchant account created successfully!')
                return redirect('merchant_account')
            except grpc.RpcError as e:
                messages.error(request, f"Failed to create merchant account: {e.details()}")
        
        # Get list of merchant accounts with pagination
        accounts_response = payment_stub.GetMerchantAccounts(
            payment_pb2.GetMerchantAccountsRequest(),
            metadata=metadata
        )
        accounts_list = list(accounts_response.accounts)
        
        # Pagination
        paginator = Paginator(accounts_list, 10)  # Show 10 accounts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # Get list of merchants for the dropdown
        merchants_response = invoice_stub.ListMerchants(Empty(), metadata=metadata)
        merchants = list(merchants_response.merchants)
        
        context = {
            'accounts': page_obj,
            'merchants': merchants
        }
        return render(request, 'merchant/merchant_account.html', context)
        
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load merchant accounts: {e.details()}")
        return render(request, 'merchant/merchant_account.html', {'accounts': [], 'merchants': []})

def edit_merchant_account(request, merchant_id):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    try:
        if request.method == 'POST':
            try:
                # Create update request
                update_request = payment_common.MerchantAccount(
                    merchant_id=merchant_id,
                    bank_name=request.POST.get('bank_name', ''),
                    bank_account_name=request.POST.get('bank_account_name', ''),
                    bank_branch_name=request.POST.get('bank_branch_name', ''),
                    bank_branch_code=request.POST.get('bank_branch_code', ''),
                    bank_account_number=request.POST.get('bank_account_number', ''),
                    bank_routing_number=request.POST.get('bank_routing_number', ''),
                    account_currency=request.POST.get('account_currency', 'USD'),
                    is_active=request.POST.get('is_active', 'false').lower() == 'true'
                )
                
                # Call the gRPC service to update account
                payment_stub.UpdateMerchant(update_request, metadata=metadata)
                messages.success(request, 'Merchant account updated successfully!')
                return redirect('merchant_account')
            except grpc.RpcError as e:
                messages.error(request, f"Failed to update merchant account: {e.details()}")
                return redirect('merchant_account')
        
        # Get merchant account details for editing
        merchant_accounts = payment_stub.GetMerchantAccounts(
            payment_pb2.GetMerchantAccountsRequest(),
            metadata=metadata
        )
        
        # Find the specific account to edit
        account_to_edit = None
        for account in merchant_accounts.accounts:
            if account.merchant_id == merchant_id:
                account_to_edit = account
                break
        
        if not account_to_edit:
            messages.error(request, "Merchant account not found")
            return redirect('merchant_account')
        
        # Get list of merchants for the dropdown
        merchants_response = invoice_stub.ListMerchants(Empty(), metadata=metadata)
        
        context = {
            'account': account_to_edit,
            'merchants': merchants_response.merchants
        }
        return render(request, 'merchant/edit_merchant_account.html', context)
        
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load merchant account: {e.details()}")
        return redirect('merchant_account')
   
def user_management(request):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    mobile_search = request.GET.get('mobile', '').strip()
    next_page_token = ""

    try:
        user_list = []
        if mobile_search:
            try:
                user = auth_stub.GetUserByMobile(
                    auth_pb2.GetUserByMobileRequest(mobile=mobile_search),
                    metadata=metadata
                )
                user_list = [user]
            except grpc.RpcError as e:
                if e.code() == grpc.StatusCode.NOT_FOUND:
                    messages.info(request, f"No user found with mobile number {mobile_search}")
                else:
                    messages.error(request, f"Search error: {e.details()}")
        else:
            page_size = 10
            next_page_token = request.GET.get('next_page_token', '')
            request_obj = auth_pb2.ListUsersRequest(page_size=page_size, page_token=next_page_token)
            response = auth_stub.ListUsers(request_obj, metadata=metadata)
            user_list = list(response.users)
            next_page_token = response.next_page_token or "" # For navigation

        paginator = Paginator(user_list, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context = {
            'users': page_obj,
            'mobile_search': mobile_search,
            'next_page_token': next_page_token
        }
        return render(request, 'merchant/user_management.html', context)

    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load users: {e.details()}")
        return render(request, 'merchant/user_management.html', {'users': []})

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

def provider(request):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    try:
        search_query = request.GET.get('search', '').strip()
        if request.method == 'POST':
            try:
                provider_request = payment_pb2.RegisterProviderRequest(
                    provider=payment_common.PaymentProvider(
                        code=request.POST.get('code'),
                        name=request.POST.get('name'),
                        type=request.POST.get('type'),
                        api_key=request.POST.get('api_key', ''),
                        is_active=request.POST.get('is_active', 'false').lower() == 'true',
                        description=request.POST.get('description', '')
                    )
                )
                payment_stub.RegisterProvider(provider_request, metadata=metadata)
                messages.success(request, 'Provider created successfully!')
                return redirect('provider')
            except grpc.RpcError as e:
                messages.error(request, f"Failed to create provider: {e.details()}")
    
        # Get list of providers with pagination
        response = payment_stub.ListProviders(
            payment_pb2.ListProvidersRequest(active_only=False),
            metadata=metadata
        )
        providers_list = list(response.providers)
        if search_query:
            providers_list = [
                p for p in providers_list 
                if (search_query.lower() in p.code.lower()) or 
                   (search_query.lower() in p.name.lower()) or
                   (search_query.lower() in p.type.lower())
            ]
        
        # Pagination
        paginator = Paginator(providers_list, 6)  # Show 10 providers per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'merchant/provider.html', {
            'providers': page_obj,  # Note the plural 'providers'
            'search_query': search_query
        })
    
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load providers: {e.details()}")
        return render(request, 'merchant/provider.html', {'providers': []})

def edit_provider(request, provider_code):
    if 'auth_token' not in request.session:
        return redirect(f"/login?next={request.path}")
    metadata = [('authorization', f'Bearer {request.session["auth_token"]}')]
    
    try:
        if request.method == 'POST':
            try:
                update_request = payment_pb2.UpdateProviderRequest(
                  provider=payment_common.PaymentProvider(
                        code=provider_code,
                        name=request.POST.get('name'),
                        type=request.POST.get('type'),
                        api_key=request.POST.get('api_key', ''),
                        is_active=request.POST.get('is_active', 'false').lower() == 'true',
                        description=request.POST.get('description', '')
                    )  
                )
                payment_stub.UpdateProvider(update_request, metadata=metadata)
                messages.success(request, 'Provider updated successfully!')
                return redirect('provider')
            except grpc.RpcError as e:
                messages.error(request, f"Failed to create provider: {e.details()}")
                return redirect('provider')
        provider_response = payment_stub.ListProviders(
            payment_pb2.ListProvidersRequest(active_only=False),
            metadata=metadata
        )
        context = {
            'provider': provider_response.provider
        }
        return render(request, 'merchant/edit_provider.html', context)
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAUTHENTICATED:
            del request.session['auth_token']
            return redirect('login')
        messages.error(request, f"Failed to load providers: {e.details()}")
        return render(request, 'merchant/provider.html', {'providers': []})
    
   