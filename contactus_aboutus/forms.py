from django import forms
from .models import contactus


class contactForm(forms.ModelForm):
    class Meta:
        model = contactus
        fields = ['contact_subject','contact_name','contact_email','contact_message']
        widgets = {
            'contact_message' : forms.Textarea(attrs={'rows':3})

        }
