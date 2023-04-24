from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
]
