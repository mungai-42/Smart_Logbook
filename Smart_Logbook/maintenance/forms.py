from django import forms
from .models import MaintenanceRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['title', 'category', 'description', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md'}),
            'category': forms.Select(attrs={'class': 'w-full p-2 border rounded-md'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-md', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-md'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
