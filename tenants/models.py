from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    on_trial = models.BooleanField(default=True)
    trial_days = models.IntegerField(default=30)
    created_on = models.DateTimeField(auto_now_add=True)

class Domain(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100, unique=True)

class TenantUser(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Assuming you have Django's User model
    is_active = models.BooleanField(default=True)  
