from django import template
from django.contrib.auth.models import User
from maintenance.models import MaintenanceRequest, Technician
from django.db.models import Count

register = template.Library()

@register.simple_tag
def get_dashboard_stats():
    total_requests = MaintenanceRequest.objects.count()
    pending = MaintenanceRequest.objects.filter(status='pending').count()
    in_progress = MaintenanceRequest.objects.filter(status='in_progress').count()
    completed = MaintenanceRequest.objects.filter(status='completed').count()
    
    total_technicians = Technician.objects.count()
    total_users = User.objects.count()
    
    # Category distribution for charts
    categories = MaintenanceRequest.objects.values('category').annotate(count=Count('category'))
    category_labels = [c['category'] for c in categories]
    category_data = [c['count'] for c in categories]
    
    return {
        'total_requests': total_requests,
        'pending': pending,
        'in_progress': in_progress,
        'completed': completed,
        'total_technicians': total_technicians,
        'total_users': total_users,
        'category_labels': category_labels,
        'category_data': category_data,
    }
