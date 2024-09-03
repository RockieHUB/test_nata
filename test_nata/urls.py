"""
URL configuration for test_nata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from pendaftaran.views import RegisterAPIView
from login.views import LoginAPIView, ProtectedAPIView
from dashboard.views import DashboardAPIView
from pelatihanku.views import PelatihankuAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPIView.as_view(), name="Pendaftaran"),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/protected/', ProtectedAPIView.as_view(), name='protected'),
    path('api/dashboard/', DashboardAPIView.as_view(), name="Dashboard"),
    path('api/pelatihanku/', PelatihankuAPIView.as_view(), name="Pelatihanku"),
]
