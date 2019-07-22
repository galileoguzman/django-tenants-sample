from django.db import models
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Client

class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'paid_until')

admin.site.register(Client, ClientAdmin)