from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = 'index'),
    path('stories/', views.stories, name ='stories'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('findyourpal/', views.findyourpal, name='findyourpal'),


]
