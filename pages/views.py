from django.shortcuts import render, redirect
from pages.models import ContactUs
from django.utils import timezone


# Create your views here.

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact_us = ContactUs(name=name, email=email, message=comment, date=timezone.now(),seen=False)
        contact_us.save()
        return redirect('contact-us')

    return render(request, 'pages/contactus_page.html')


def aboutus(request):
    return render(request, 'pages/aboutus_page.html')
