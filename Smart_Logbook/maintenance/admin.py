from django.contrib import admin
from .models import Technician, MaintenanceRequest

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'phone')

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'room_number', 'category', 'status', 'tenant', 'technician', 'created_at')
    list_filter = ('status', 'category', 'technician', 'created_at')
    search_fields = ('title', 'description', 'room_number', 'tenant__username')
    date_hierarchy = 'created_at'
