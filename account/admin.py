from django.contrib import admin
from .models import BusinessUser

# Register your models here.
class BusinessUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'business_name', 'industry', 'is_entity_display', 'is_disbursment_display', 'account_number_display', 'operation_display')  # Add display fields for boolean
    search_fields = ('email', 'business_name', 'phone_number')
    ordering = ('business_name',)
    
    # Custom display for boolean fields
    def is_entity_display(self, obj):
        return 'Yes' if obj.is_entity else 'No'
    is_entity_display.short_description = 'Is Entity'  # Column header in admin

    def is_disbursment_display(self, obj):
        return 'Yes' if obj.is_disbursment else 'No'
    is_disbursment_display.short_description = 'Is Disbursement'

    def account_number_display(self, obj):
        return 'Yes' if obj.account_number else 'No'
    account_number_display.short_description = 'Account Number Required'

    def operation_display(self, obj):
        return 'Yes' if obj.operation else 'No'
    operation_display.short_description = 'Requires Packages'
    
admin.site.register(BusinessUser, BusinessUserAdmin)
