from django.db import models

# Create your models here.
class story(models.Model):

    def __str__(self):
        return self.story_title
    story_title = models.CharField(max_length=200)
    story_desc = models.CharField(max_length=2000)
    nickname = models.CharField(max_length=100)
    story_image = models.CharField(max_length=500, default='https://cdn-icons-png.flaticon.com/512/169/169503.png')
