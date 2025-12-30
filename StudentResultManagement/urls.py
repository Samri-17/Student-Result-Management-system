"""
URL configuration for StudentResultManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resultapp.views import admin_login as admin_login, create_class as create_class, index as index, render as render ,admin_dashboard as admin_dashboard, admin_logout as admin_logout, manage_class
from resultapp.views import edit_class as edit_class

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='home'), #localhost paxi khali huda index viewa call hunxa
    path('admin-login/',admin_login, name='admin_login'),
    path('admin_dashboard/',admin_dashboard, name='admin_dashboard'), #admin home page ko lagi
    path('create_class/',create_class, name='create_class'),
    path('admmin_logout/',admin_logout, name='admin_logout'),
    path('manage_class/',manage_class, name='manage_class'),
    path('edit_class/<int:class_id>/',edit_class, name='edit_class') 
]
