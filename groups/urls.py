from django.urls import path
from . import views

app_name = 'groups'
urlpatterns = [
    path('', views.main, name="main"),
    path('certify/', views.certify, name="certify"),
]
