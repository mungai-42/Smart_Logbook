from django import forms
from .models import MaintenanceRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['category', 'room_number', 'title', 'description', 'photo']
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full bg-white/10 border border-gray-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'room_number': forms.TextInput(attrs={'class': 'w-full bg-white/10 border border-gray-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'e.g., Room 12, House B4'}),
            'title': forms.TextInput(attrs={'class': 'w-full bg-white/10 border border-gray-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Brief summary of the issue'}),
            'description': forms.Textarea(attrs={'class': 'w-full bg-white/10 border border-gray-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 4, 'placeholder': 'Describe the issue in detail...'}),
            'photo': forms.FileInput(attrs={'class': 'w-full bg-white/10 border border-gray-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
