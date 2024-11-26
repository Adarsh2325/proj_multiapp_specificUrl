from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def caption(request):
    return HttpResponse('''<h1>Dhuniya Hila Denge Hum....</h1>
    <img src=https://www.mykhel.com/img/2020/02/mumbai-indians-celebrate-1582277716.jpg>''')
