from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.main_logout, name="main_logout"),
    path('login/', views.main_login, name="main_login"),
    path('add_goal/', views.add_goal, name="add_goal"),
]