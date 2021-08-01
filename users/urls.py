from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('mypage_update', views.mypage_update, name="mypage_update"),
]
