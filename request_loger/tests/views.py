
from rest_framework.response import Response
from rest_framework.views import APIView

from request_loger.mixins import LoggingMixin


class MockNoLoggingView(APIView):
    def get(self, request):
        return Response("no logging")


class MockLoggingView(LoggingMixin, APIView):
    def get(self, request):
        return Response("with logging")

    def post(self, request):
        return Response("with logging")
