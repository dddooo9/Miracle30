from django.urls import path
from . import views

app_name = 'groups'
urlpatterns = [
    path('<int:goal_id>', views.main, name="main"),
    path('<int:goal_id>/certify/', views.certify, name="certify"),
    path('group_list/', views.group_list, name="group_list"),
    path('group_detail/', views.group_detail, name="group_detail"),
    path('make_group/', views.make_group, name="make_group"),
    path('<int:goal_id>/date_check', views.date_check, name="date_check"),
    path('<int:goal_id>/<int:user_id>/delete_member', views.delete_member, name="delete_member"),
    
]
