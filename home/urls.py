from . import views
from django.urls import path

app_name='home'
urlpatterns = [
    path("", views.index, name = 'index'),
    path('stories', views.stories, name ='stories'),
    path('findyourpal', views.findyourpal, name='findyourpal'),
    path('add_story', views.add_story, name ='add_story'),

]
