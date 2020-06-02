from django.shortcuts import render
from topic.models import Topic
from comic.models import Chapter
# Create your views here.


def home(request):
    topics = Topic.objects.all().order_by('-created_time')[:5]
    chapters = Chapter.objects.all().order_by('-chapter_number')[:5]
    context = {
        'topics': topics,
        'chapters': chapters,
    }
    return render(request, 'home.html', context)


