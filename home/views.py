from django.shortcuts import render
from django.http import HttpResponse
from .models import story
from django.template import loader

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'home/index.html', context)

def stories(request):
    story_list = story.objects.all()
    context = {
        'story_list': story_list,

    }

    return render(request, 'home/stories.html', context)
