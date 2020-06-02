from django.contrib import admin
from .models import TopicType,Topic
# Register your models here.


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic_type', 'content', 'created_time', 'creator', 'last_modified')


@admin.register(TopicType)
class TopicTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
