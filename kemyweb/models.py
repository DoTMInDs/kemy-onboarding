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


class BusinessInfo(models.Model):
    business_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=50,choices=INDUSTRY_CHOICES)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50,verbose_name="First name",null=True,blank=True)
    last_name = models.CharField(max_length=50,verbose_name="Last name",null=True,blank=True)
    product_category = models.CharField(max_length=50,choices=PRODUCT_CATEGORY_CHOICES,blank=True,null=True,verbose_name="What category does your product or service belong to?")
    physical_address = models.TextField(blank=True, null=True,verbose_name="Physical address")
    organization = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.business_name