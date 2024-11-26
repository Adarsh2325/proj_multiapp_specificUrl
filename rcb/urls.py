from django.urls import path

from rcb.views import *

urlpatterns=[
    path('caption/',caption,name='caption'),
    

]