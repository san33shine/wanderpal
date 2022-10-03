from django.db import models

# Create your models here.
class story(models.Model):

    def __str__(self):
        return self.story_title
    story_title = models.CharField(max_length=200)
    story_desc = models.CharField(max_length=2000)
    nickname = models.CharField(max_length=100)
    story_image = models.ImageField(null=True, blank=True, upload_to='images/')


class profile(models.Model):
    def __str__(self):
        return self.profile_name
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Others')
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
    #part to upload picture, think of video face recognition
