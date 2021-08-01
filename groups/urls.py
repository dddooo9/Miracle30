from django.urls import path
from . import views

app_name = 'groups'
urlpatterns = [
    path('', views.main, name="main"),
    path('certify_image/', views.certify_image, name="certify_image"),
    path('certify_text/', views.certify_text, name="certify_text"),
    path('certify_figure/', views.certify_figure, name="certify_figure"),
]
