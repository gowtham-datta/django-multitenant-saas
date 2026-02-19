from django.contrib import admin
from .models import Tenant, Domain, TenantUser

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant')

@admin.register(TenantUser)
class TenantUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'tenant')