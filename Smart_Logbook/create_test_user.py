import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smls_project.settings')
django.setup()

from django.contrib.auth.models import User
try:
    user = User.objects.get(username='testuser')
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("Test user updated to Admin")
except User.DoesNotExist:
    User.objects.create_superuser('testuser', 'test@example.com', 'password123')
    print("Admin user created")
