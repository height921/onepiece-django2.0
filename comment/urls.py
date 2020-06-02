#!python
# -*- encoding:utf-8 -*-
# Created by admin at 2020/5/24

from django.urls import path
from . import views
app_name = 'comment'
urlpatterns = [
    path('submit_comment', views.submit_comment, name='submit_comment'),
]
