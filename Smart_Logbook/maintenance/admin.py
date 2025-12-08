from django.contrib import admin
from .models import Technician, MaintenanceRequest

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'phone')

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'tenant', 'technician', 'created_at')
    list_filter = ('status', 'category', 'technician')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
