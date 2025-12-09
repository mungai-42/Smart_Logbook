import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smls_project.settings')
django.setup()

from django.contrib.auth.models import User
try:
    user = User.objects.get(username='testuser')
    user.first_name = "System"
    user.last_name = "Admin"
    user.save()
    print("Test user updated with name: System Admin")
except User.DoesNotExist:
    print("User not found")
