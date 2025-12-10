from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('issues/', views.dashboard, name='dashboard'),
    path('issues/create/', views.create_issue, name='create_issue'),
    path('issues/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('', views.home, name='home'),
]
