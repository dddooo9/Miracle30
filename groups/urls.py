from django.urls import path
from . import views

app_name = 'groups'
urlpatterns = [
    path('<int:goal_id>', views.main, name="main"),
    path('<int:goal_id>/certify/', views.certify, name="certify"),
    path('<int:goal_id>/personal/', views.personal, name="personal"),
    path('<int:goal_id>/show_certify/', views.show_certify, name="show_certify"),
    path('group_list/', views.group_list, name="group_list"),
    path('group_detail/', views.group_detail, name="group_detail"),
    path('make_group/', views.make_group, name="make_group")
]
