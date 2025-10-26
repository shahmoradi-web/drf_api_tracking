from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.


class Home(APIView):
    def get(self, request):
        return Response({'message': 'Hello World!'})
