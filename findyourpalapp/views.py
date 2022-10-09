from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def fyp_index(request):
    context = {

    }
    return render(request, 'findyourpalapp/fyp_index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('findyourpalapp:fyp_index')
    else:
        form = RegisterForm()
    return render(request, 'findyourpalapp/register.html', {'form':form})
