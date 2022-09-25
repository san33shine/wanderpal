from django.db import models

# Create your models here.
class story(models.Model):

    def __str__(self):
        return self.story_title
    story_title = models.CharField(max_length=200)
    story_desc = models.CharField(max_length=2000)
    nickname = models.CharField(max_length=100)
    story_image = models.CharField(max_length=500, default='https://cdn-icons-png.flaticon.com/512/169/169503.png')

class profile(models.Model):
    def __str__(self):
        return self.profile_name
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Others')
    )
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    socialmedia = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    travel_itinerary = models.CharField(max_length=1000)
    about_yourself = models.CharField(max_length=100)
    #part to upload picture, think of video face recognition
