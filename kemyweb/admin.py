from django.contrib import admin
from .models import BusinessInfo

class BusinessInfoAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'industry', 'email', 'physical_address', 'product_category')

# Register your models here.
admin.site.register(BusinessInfo,BusinessInfoAdmin)