from . import views
from django.urls import path

app_name ='contactus_aboutus'
urlpatterns = [
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),


]
