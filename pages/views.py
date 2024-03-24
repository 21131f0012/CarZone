from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    teams = Team.objects.all()  # Get all the teams
    data = {
        'teams': teams,
        }
    return render(request,'pages/home.html',data)


def about(request):
    teams = Team.objects.all()  # Get all the teams
    data = {
        'teams': teams,
        }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')
