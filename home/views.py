from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import story, profile
from django.template import loader
from .forms import storyForm

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

def aboutus(request):
    context = {

    }
    return render(request, 'home/aboutus.html', context)

def contactus(request):
    context = {

    }
    return render(request, 'home/contactus.html', context)

def findyourpal(request):
    context = {

    }
    return render(request, 'home/findyourpal.html', context)



def add_story(request):
    form = storyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'home/add_story.html', {'form':form})
