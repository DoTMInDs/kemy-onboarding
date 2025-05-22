from django.apps import AppConfig
import grpc
from django.conf import settings

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    auth_channel = None

    def ready(self):
        if not self.auth_channel:
            self.auth_channel=grpc.insecure_channel(settings.AUTH_GRPC_SERVER)
