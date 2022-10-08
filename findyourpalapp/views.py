from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail

# Create your views here.
def fyp_login(request):
    context = {

    }
    return render(request, 'findyourpalapp/fyp_login.html', context)
