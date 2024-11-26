from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def caption(request):
    return HttpResponse('''
    <h1>WhistlePodu....</h1>
    <img src=https://s01.sgp1.digitaloceanspaces.com/large/882306-xwnwhbbtwr-1526703223.jpg>
    ''')


