from django.shortcuts import render,redirect
from account.forms import BusinessContactForm
from django.contrib import messages


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
    return render(request, 'merchant/dashboard.html')

def merchant(request):
    return render(request, 'merchant/merchant.html')

def merchant_provider(request):
    return render(request, 'merchant/merchant_provider.html')

def merchant_account(request):
    return render(request, 'merchant/merchant_account.html')

def user_management(request):
    return render(request, 'merchant/user_management.html')

def provider(request):
    return render(request, 'merchant/provider.html')
