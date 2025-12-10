import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smls_project.settings')
django.setup()

from django.contrib.auth.models import User

try:
    user = User.objects.get(username='Samuel')
    user.username = 'Admin'
    user.save()
    print("Successfully renamed user 'Samuel' to 'Admin'.")
except User.DoesNotExist:
    print("User 'Samuel' not found. Checking if 'Admin' already exists...")
    if User.objects.filter(username='Admin').exists():
        print("User 'Admin' already exists.")
    else:
        print("Neither 'Samuel' nor 'Admin' users found.")
