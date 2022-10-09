from . import views
from django.urls import path


app_name='findyourpalapp'
urlpatterns = [
    # path('findyourpalapp/', views.fyp_login, name='findyourpalapp'),
    path('fyp_login/', views.fyp_login, name ='fyp_login'),
    path('register/', views.register, name='register'),

]
