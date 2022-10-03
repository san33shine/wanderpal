from django.db import models

# Create your models here.
class contactus(models.Model):
    def __str__(self):
        return self.contact_subject
    contact_subject = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=1000)
