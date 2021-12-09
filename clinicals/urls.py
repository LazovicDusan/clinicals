"""clinicals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from clinicalsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', views.home),
    path('start/accounts/', include('django.contrib.auth.urls')),
    path('start/register/', views.register),
    path('patient/', views.patientListView, name='index'),
    # path('patient/', views.PatientListView.as_view(), name='index'), # name is used in reverse_lazy funct in views
    path('patient/create/', views.PatientCreateView.as_view()),      # so you know where to go
    path('patient/update/<int:pk>/', views.PatientUpdateView.as_view()),
    path('patient/delete/<int:pk>/', views.PatientDeleteView.as_view()),
    path('patient/addData/<int:pk>/', views.addData),
    path('patient/analyze/<int:pk>', views.analyze)
]
