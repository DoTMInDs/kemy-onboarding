from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('invoice/', views.invoice, name='invoice'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_management/', views.user_management, name='user_management'),
    path('merchant/', views.merchant, name='merchant'),
    path('merchant/invoices/', views.merchant_invoice, name='merchant_invoice'),
    path('merchant/payments/', views.merchant_payment, name='merchant_payment'),
]
