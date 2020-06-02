#!python
# -*- encoding:utf-8 -*-
# Created by admin at 2020/5/27


from django.urls import path
from . import views

urlpatterns = [
    path('like_change/', views.like_change, name='like_change')
]
