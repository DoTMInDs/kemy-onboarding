from django.apps import AppConfig
import grpc
from django.conf import settings



class KemywebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kemyweb'
    invoice_channel = None
    auth_channel = None

    def ready(self):
        if not self.invoice_channel:
            self.invoice_channel=grpc.insecure_channel(settings.INVOICE_GRPC_SERVER)
            
        if not self.auth_channel:
            self.auth_channel=grpc.insecure_channel(settings.AUTH_GRPC_SERVER)
        
        