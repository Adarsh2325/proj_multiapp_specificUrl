from django.urls import path

from csk.views import *

urlpatterns=[
    path('caption/',caption,name='caption'),
    
]