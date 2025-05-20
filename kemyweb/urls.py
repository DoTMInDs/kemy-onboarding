from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('invoice/', views.invoice, name='invoice'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_management/', views.user_management, name='user_management'),
    path('merchant/', views.merchant, name='merchant'),
    path('merchant/provider/', views.merchant_provider, name='merchant_provider'),
    path('merchant/accounts/', views.merchant_account, name='merchant_account'),
    path('provider/', views.provider, name='provider'),
]
