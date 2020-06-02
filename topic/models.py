from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TopicType(models.Model):
    type_name = models.CharField(max_length=20)
    type_introduction = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='topic_type_images/', null=True, blank=True)

    def __str__(self):
        return self.type_name


class Topic(models.Model):
    title = models.CharField(max_length=255)
    topic_type = models.ForeignKey(TopicType, on_delete=models.CASCADE,related_name='topic_type')
    content = RichTextUploadingField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator',null=True,blank=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<Topic:%s>" % self.title
