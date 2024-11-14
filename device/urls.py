from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_page, name='device_page'),
    path("dashboard", views.deviceDashboardview, name="dashboard"),
    path("adddevice", views.add_device, name="adddevice"),
    path("devicelist", views.devicelistview, name="devicelist"),
    path('toggle-device/<str:device_id>/', views.toggle_device, name='toggle_device'),
    path('delete-device/<str:device_id>/', views.delete_device, name='delete_device'),


]