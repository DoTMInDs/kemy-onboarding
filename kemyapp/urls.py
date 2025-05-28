from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_management/', views.user_management, name='user_management'),
    path('user_management/edit/<int:pk>/', views.edit_user_management, name='edit_user_management'),
    path('merchant/', views.merchant, name='merchant'),
    path('merchant/detail/<int:merchant_id>/', views.merchant_detail, name='merchant_detail'),
    path('merchant/edit/<int:merchant_id>/', views.edit_merchant, name='edit_merchant'),
    path('merchant_provider/edit/<int:merchant_id>/', views.edit_merchant_provider, name='edit_merchant_provider'),
    path('merchant/delete/<int:merchant_id>/', views.delete_merchant, name='delete_merchant'),
    path('merchant/provider/', views.merchant_provider, name='merchant_provider'),
    path('merchant/accounts/', views.merchant_account, name='merchant_account'),
    path('merchant/account/edit/<int:merchant_id>/', views.edit_merchant_account, name='edit_merchant_account'),
    path('provider/', views.provider, name='provider'),
    path('provider/<str:provider_code>/edit/', views.edit_provider, name='edit_provider'),
]
