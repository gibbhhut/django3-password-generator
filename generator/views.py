import random
import string

from django.shortcuts import render
#--from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend(string.punctuation)
    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
