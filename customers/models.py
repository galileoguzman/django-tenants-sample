from datetime import timedelta
from django.utils import timezone
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

def one_month_from_today():
    return timezone.now() + timedelta(days=30)


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField(default=one_month_from_today, blank=True, null=True)
    on_trial = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    pass