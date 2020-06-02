#!python
# -*- encoding:utf-8 -*-
# Created by admin at 2020/5/27
from django import template
from comment.models import Comment
from topic.models import Topic
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.simple_tag
def get_topic_count(user):
    return Topic.objects.filter(creator=user).count()


@register.simple_tag
def get_topic_list(user):
    return Topic.objects.filter(creator=user).order_by('-created_time')


@register.simple_tag
def get_comment_count(user):
    return Comment.objects.all().count()
    # return Comment.objects.filter(comment_user=user, parent=None).count()


@register.simple_tag
def get_comment_list(user):
    comments = Comment.objects.filter(comment_user=user, parent=None)
    comments = Comment.objects.all()
    return comments


@register.simple_tag
def get_topic(object_id):
    return Topic.objects.get(pk=object_id)
    # return Topic.objects.filter(pk=comment.object_id)

