from django.shortcuts import render, get_object_or_404
from .models import Topic, TopicType
from .forms import TopicForm
from django.http import JsonResponse

# Create your views here.


def topics_with_type(request, type_pk):
    topic_type = get_object_or_404(TopicType,pk=type_pk)
    topics = Topic.objects.filter(topic_type=topic_type)
    context = {
        'topics': topics,
        'topic_type': topic_type,
    }
    return render(request, 'topics_with_type.html', context)


def topic_index(request):
    if request.method == 'POST':
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            topic = topic_form.save(commit=False)
            topic.creator = request.user
            topic.save()

    topics = Topic.objects.all().order_by('-created_time')
    context = {
        'topics': topics,
        'topic_form': TopicForm(),

    }
    return render(request, 'topic_index.html', context)


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    context = {
        'topic': topic,
    }
    return render(request, 'topic_detail.html', context)


# def add_topic(request):
#     topic_form = TopicForm(request.POST)
#     data={}
#     if topic_form.is_valid():
#         topic = topic_form.save(commit=False)
#         topic.creator = request.user
#         # topic = Topic()
#         # topic.content=topic_form.cleaned_data['content']
#         # topic.title=topic_form.cleaned_data['title']
#         # topic.creator=topic_form.cleaned_data['user']
#         # topic.topic_type=topic_form.cleaned_data['topic_type']
#         data['status']='SUCCESS'
#         # data['username'] = topic.creator
#         # data['created_time'] = topic.created_time
#         # data['pk'] = topic.pk
#         topic.save()
#
#     else:
#         data['status'] = 'ERROR'
#         data['message'] = list(topic_form.errors())[0][0]
#
#     return JsonResponse(data, safe=False)