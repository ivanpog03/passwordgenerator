from django.shortcuts import render
from django.http import *
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters=list('abcdefghijklmnopqrstuwvyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHHIJKLMNOPQRSTUWVYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('ABCDEFGHHIJKLMNOPQRSTUWVYZ'))
    if request.GET.get('special'):
        characters.extend(list('ABCDEFGHHIJKLMNOPQRSTUWVYZ'))
    length=int(request.GET.get('length'))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})
