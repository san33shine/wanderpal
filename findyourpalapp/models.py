from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'profile_pictures/profilepic.png', upload_to='profile_pictures')
    location = models.CharField(max_length = 200)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    socialmedia = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    nationality = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    travel_itinerary = models.CharField(max_length=1000)
    about_yourself = models.CharField(max_length=100)
    pal_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pal_nationality = models.CharField(max_length=1, choices=TRUE_FALSE_CHOICES)

    # part to upload picture, think of video face recognition

    def __str__(self):
        return self.user.username
