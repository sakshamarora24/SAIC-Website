from django.shortcuts import render, redirect
from website import settings
from .models import Contact
from profiles.models import Unregistered_subscriber


def home(request):
    if request.method == 'POST':
        email = request.POST['sub_email']
        url = request.META['HTTP_REFERER']
        if request.user.is_authenticated:
            request.user.newsletter.isSubscribed = True
            request.user.newsletter.save()
            return redirect(url)
        unregistered_subscriber = Unregistered_subscriber(email=email)
        unregistered_subscriber.save()
        return redirect(url)
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')


def about(request):
    return render(request, 'about.html')


def AIM(request):
    return render(request, 'AIM.html')


def convocation(request):
    return render(request, 'convocation.html')


def exordium(request):
    return render(request, 'Exordium.html')


def GLS(request):
    return render(request, 'GLS.html')


def scribble(request):
    return render(request, 'scribble.html')


def troubleshoot(request):
    return render(request, 'troubleshoot.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return render(request, 'contact.html', {'message': 'Message sent successfully.'})
        

    return render(request, 'contact.html')

def covidhelp(request):
    return render(request, 'covidhelp.html')