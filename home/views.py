from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import story, profile
from django.template import loader
from .forms import storyForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'home/index.html', context)

def stories(request):
    story_list = story.objects.all().order_by('-created')
    context = {
        'story_list': story_list,

    }

    return render(request, 'home/stories.html', context)



def findyourpal(request):
    context = {

    }
    return render(request, 'home/findyourpal.html', context)



def add_story(request):
    form = storyForm(request.POST, request.FILES)

    if form.is_valid():
        form.instance.owner = request.user
        form.save()
        return redirect('home:stories')

    return render(request,'home/add_story.html', {'form':form})
