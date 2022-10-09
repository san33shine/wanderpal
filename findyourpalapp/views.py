from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def fyp_login(request):
    context = {

    }
    return render(request, 'findyourpalapp/fyp_login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('findyourpalapp:fyp_login')
    else:
        form = UserCreationForm()
    return render(request, 'findyourpalapp/register.html', {'form':form})
