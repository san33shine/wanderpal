from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name='findyourpalapp'
urlpatterns = [
    path('fyp_index/', views.fyp_index, name ='fyp_index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name ="findyourpalapp/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ="findyourpalapp/logout.html"), name='logout'),


]
