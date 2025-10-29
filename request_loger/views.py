from django.shortcuts import render
from rest_framework.response import Response

from request_loger.base_mixins import BaseLogginMixin


# Create your views here.


class Home(BaseLogginMixin,APIView):

    logging_methods = ['GET', 'POST']
    def get(self, request):
        return Response({'message': 'Hello World!'})
