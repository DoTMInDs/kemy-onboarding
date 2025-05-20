from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BusinessUser
from django.contrib.auth.forms import AuthenticationForm
from kemyweb.models import BusinessInfo

class BusinessContactForm(forms.ModelForm):
    class Meta:
        model = BusinessInfo    
        fields = [
            'business_name',
            'industry',
            'email',
            'first_name',
            'last_name',
            'product_category',
            'physical_address',
            'organization',
            'message',
        ] 