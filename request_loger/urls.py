from django.urls import path
from .views import *

app_name = 'request_loger'

urlpatterns =[
    path('', Home, name='Home'),
]