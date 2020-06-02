#!python
# -*- encoding:utf-8 -*-
# Created by admin at 2020/5/27


from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user_info/', views.user_info, name='user_info'),
    path('register/', views.register, name='register'),
    path('user_join', views.user_join, name='user_join'),
]
