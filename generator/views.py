from django.shortcuts import render
from django.http import *


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
