from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def caption(request):
    return HttpResponse('''<h1>Ee Sala Cup Namde....</h1>
    <img src=https://cricketaddictor.com/wp-content/uploads/2023/11/Royal-Challengers-Banglaore-RCB.webp>''')
