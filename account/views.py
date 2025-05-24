from django.shortcuts import render, redirect
from django.contrib import messages
from django.apps import apps
from google.protobuf.empty_pb2 import Empty
from v1.auth import auth_pb2_grpc,auth_pb2

auth_channel = apps.get_app_config('account').auth_channel
auth_stub=auth_pb2_grpc.AuthStub(auth_channel)

# Create your views here.
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