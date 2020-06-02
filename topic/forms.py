#!python
# -*- encoding:utf-8 -*-
# Created by admin at 2020/5/28

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Topic, TopicType


class TopicForm(forms.ModelForm):
    title = forms.CharField(
        label='标题',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'bg-light form-control',
        })
    )
    # content = forms.CharField(widget=CKEditorWidget(config_name='topic_ckeditor'),)
    content = forms.CharField(label='内容', widget=CKEditorUploadingWidget(config_name='topic_ckeditor'))
    topic_type = forms.ModelChoiceField(
        label='分类',
        queryset=TopicType.objects.all(),
        widget=forms.Select(attrs={
            'class': 'bg-light custom-select',
        })
    )
    class Meta:
        model = Topic
        fields = ['title', 'content', 'topic_type']


    # def __init__(self, *args, **kwargs):
    #     if 'creator' in kwargs:
    #         self.creator = kwargs.pop('creator')
    #     super(TopicForm, self).__init__(*args, **kwargs)
    #
    # def clean(self):
    #     if self.user.is_authenticated:
    #         self.cleaned_data['creator'] = self.creator
    #     else:
    #         raise forms.ValidationError('用户尚未登录')

# class TopicForm(forms.Form):
#     topic_type = forms.ChoiceField(widget=forms.RadioSelect, choices=TopicType.objects.all())
#     title = forms.CharField(widget=forms.CharField)
#     content = forms.CharField(widget=CKEditorWidget(config_name='topic_ckeditor'))
#
#     def __init__(self, *args, **kwargs):
#         if 'user' in kwargs:
#             self.user = kwargs.pop('user')
#         super(TopicForm, self).__init__(*args, **kwargs)
#
#     def clean(self):
#         if self.user.is_authenticated:
#             self.cleaned_data['user'] = self.user
#         else:
#             raise forms.ValidationError('用户尚未登录')