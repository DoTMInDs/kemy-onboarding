from django.db import models

# Create your models here.
INDUSTRY_CHOICES = [
    ('agriculture', 'Agriculture & Agro-processing'),
    ('banking', 'Banking & Finance'),
    ('construction', 'Construction & Real Estate'),
    ('education', 'Education & Training'),
    ('health', 'Healthcare & Pharmaceuticals'),
    ('hospitality', 'Hospitality & Tourism'),
    ('manufacturing', 'Manufacturing'),
    ('mining', 'Mining & Natural Resources'),
    ('retail', 'Retail & E-commerce'),
    ('technology', 'Technology & IT Services'),
    ('telecom', 'Telecommunications'),
    ('transport', 'Transportation & Logistics'),
    ('utilities', 'Utilities & Energy'),
    ('other', 'Other Services'),
]
PRODUCT_CATEGORY_CHOICES = [
    ('airtime', 'Airtime - Internet'),
    ('association', 'Association and Organization'),
    ('church', 'Church'),
    ('bank', 'Bank Integration'),
    ('goods', 'Goods and Services'),
    ('healthcare', 'Healthcare'),
    ('insurance', 'Insurance'),
    ('investments', 'Investments'),
    ('schoolfees', 'School Fees'),
    ('utility', 'Utility'),
]
SETTLEMENT_DESTINATION_CHOICES = [
    ('mobile_mony', 'Mobile Money'),
    ('bank', 'Bank'),
]
MOBILE_MONEY_CHOICES = [
    ('mtn', 'MTN Mobile Money'),
    ('telecel', 'Telecel Cash'),
    ('airteltigo', 'AirtelTigo Money'),
]
SERVICE_CHARGE_CHOICES = [
    ('split', 'Split - 1% customer, 0.5% Business'),
    ('business', 'Business - 1.5%'),
    ('customer', 'Customer - 1.5%'),
]
SETTLEMENT_METHOD_CHOICES = [
    ('days', 'After two days'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly')
]

class BusinessUser(models.Model):
    business_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=50,choices=INDUSTRY_CHOICES)
    email = models.EmailField(unique=True)
    product_category = models.CharField(max_length=50,choices=PRODUCT_CATEGORY_CHOICES,blank=True,null=True,verbose_name="What category does your product or service belong to?")
    phone_number = models.CharField(max_length=20)
    sales_rep = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Rep Who Referred Kemy to You?")
    physical_address = models.TextField(blank=True, null=True,verbose_name="Physical address")
    monthly_transaction_size = models.CharField(max_length=100, blank=True, null=True, verbose_name="How much would you say you transact monthly?")
    company_logo = models.ImageField(upload_to='logos/', blank=True)
    is_entity = models.BooleanField(default=False)
    is_disbursment = models.BooleanField(default=False)
    director_id = models.ImageField(upload_to='images',blank=True)
    settlement_money = models.CharField(
                                max_length=50,
                                choices=SETTLEMENT_DESTINATION_CHOICES,
                                blank=True,
                                null=True,
                                verbose_name="Where should you settle money to be sent to?"
                                )
    mobile_money_network = models.CharField(max_length=50,choices=MOBILE_MONEY_CHOICES,blank=True,null=True)
    mobile_number = models.CharField(max_length=15,null=True)
    account_number = models.BooleanField(
                            default=False,
                            verbose_name='Do your customers require an account number / identified to make payment or can anyone pay?')
    operation = models.BooleanField(default=False,
                                         verbose_name='Do you operate a business that requires your customers to pay for packages?')
    max_payment_amount = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Maximum payment amount', null=True)
    min_payment_amount = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Minimum payment amount',null=True)
    service_charge = models.CharField(
                                max_length=50,
                                choices=SERVICE_CHARGE_CHOICES,
                                blank=True,
                                null=True,
                                verbose_name="Who bears the service charge?"
                                )
    settlement_method = models.CharField(
                                max_length=50,
                                choices=SETTLEMENT_METHOD_CHOICES,
                                blank=True,
                                null=True,
                                verbose_name="How frequenty do you want to be settled?"
                                )
    def __str__(self):
        return self.business_name
    

    
    
    
    
    