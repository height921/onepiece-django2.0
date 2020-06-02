from django.shortcuts import render
from django.http import HttpResponse
from .models import Chapter
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def display_detail(request, chapter, number):
    obj = Chapter.objects.get(chapter_number=chapter)
    try:
        previous_chapter = Chapter.objects.get(chapter_number=chapter-1)
    except ObjectDoesNotExist:
        previous_chapter = None
    try:
        next_chapter = Chapter.objects.get(chapter_number=chapter+1)
    except ObjectDoesNotExist:
        next_chapter = None
    context = {
        'obj': obj,
        'number': number,
        'previous_chapter': previous_chapter,
        'next_chapter': next_chapter,
    }
    return render(request, 'chapter_detail.html', context)


def comic_index(request):
    chapters = Chapter.objects.all().order_by('-chapter_number')
    context = {
        'chapters': chapters,
    }
    return render(request, 'comic_index.html', context)