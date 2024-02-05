from django.urls import path
from . import views

urlpatterns = [
    path('contact-us', views.contactus, name='contact-us'),
    path('about-us', views.aboutus, name='about-us'),
]
