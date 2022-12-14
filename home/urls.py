from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('gallery/',views.gallery, name='gallery'),
    path('about/',views.about, name='about'),
    path('AIM/',views.AIM, name='AIM'),
    path('convocation/',views.convocation, name='convocation'),
    path('exordium/',views.exordium, name='exordium'),
    path('GLS/',views.GLS, name='GLS'),
    path('scribble/',views.scribble, name='scribble'),
    path('troubleshoot/',views.troubleshoot, name='troubleshoot'),
    path('contact/',views.contact, name='contact'),
    path('covidhelp/',views.covidhelp, name='covidhelp')
]