from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, MaintenanceRequestForm
from .models import MaintenanceRequest

def home(request):
    return render(request, 'maintenance/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'maintenance/register.html', {'form': form})

@login_required
def dashboard(request):
    issues = MaintenanceRequest.objects.filter(tenant=request.user).order_by('-created_at')
    return render(request, 'maintenance/dashboard.html', {'issues': issues})

@login_required
def create_issue(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.tenant = request.user
            issue.save()
            return redirect('dashboard')
    else:
        form = MaintenanceRequestForm()
    return render(request, 'maintenance/issue_form.html', {'form': form})

@login_required
def issue_detail(request, pk):
    issue = get_object_or_404(MaintenanceRequest, pk=pk)
    return render(request, 'maintenance/issue_detail.html', {'issue': issue})
