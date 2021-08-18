from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.main_logout, name="main_logout"),
    path('login/', views.main_login, name="main_login"),
    path('goal_main/', views.goal_main, name="goal_main"),
    path('goal_detail/<int:goal_id>', views.goal_detail, name="goal_detail"),
    path('add_goal/', views.add_goal, name="add_goal"),
    path('create_goal/', views.create_goal, name="create_goal"),
    path('update_goal/<int:goal_id>', views.update_goal, name="update_goal"),
]