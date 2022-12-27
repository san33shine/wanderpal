from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class story(models.Model):

    def __str__(self):
        return self.story_title
    story_title = models.CharField(max_length=200)
    story_desc = models.CharField(max_length=2000)
    nickname = models.CharField(max_length=100)
    story_image = models.ImageField(null=True, blank=True, upload_to='story_images/', default='story_images/default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    story_country = CountryField(blank_label='(select country)')


