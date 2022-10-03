from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contactus
from django.template import loader
from .forms import contactForm
from django.core.mail import send_mail

# Create your views here.
def aboutus(request):
    context = {

    }
    return render(request, 'contactus_aboutus/aboutus.html', context)

def contactus(request):
    form = contactForm(request.POST)

    if form.is_valid():
        contact_subject = form.cleaned_data['contact_subject']
        contact_message = form.cleaned_data['contact_message']
        contact_name = form.cleaned_data['contact_name']
        recipients = ['sanchua1012@gmail.com']
        form.save()

        send_mail(contact_subject, contact_message, contact_name, recipients)
        return redirect('contactus_aboutus:contactus')
    return render(request, 'contactus_aboutus/contactus.html', {'form':form})
