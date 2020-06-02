#!python
# -*- encoding:utf-8 -*-
# Created by admin at 2020/5/24

from django.urls import path, include
from . import views
app_name = 'topic'
urlpatterns = [
    path('', views.topic_index, name='topic_index'),
    path('<int:pk>', views.topic_detail, name='topic_detail'),
    # path('add_topic', views.add_topic, name='add_topic'),
    path('type/<int:type_pk>', views.topics_with_type, name='topisc_with_type'),
]
