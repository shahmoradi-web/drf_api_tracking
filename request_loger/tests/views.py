from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
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

class MockExplicitLoggingView(LoggingMixin, APIView):
    logging_methods = ["POST"]

    def get(self, request):
        return Response("no logging")

    def post(self, request):
        return Response("with logging")

class MockSensitiveFieldsLoggingView(LoggingMixin, APIView):
    sensitive_fields = {"mY_fiEld"}

    def get(self, request):
        return Response("with logging")


class MockInvalidCleanedSubstituteLoggingView(LoggingMixin, APIView):
    CLEANED_SUBSTITUTE = 1

class MockCustomCheckLoggingView(LoggingMixin, APIView):
    def should_log(self, request, response):
        """
        Log only if response contains 'log'
        """
        return "log" in response.data

    def get(self, request):
        return Response("with logging")

    def post(self, request):
        return Response("no recording")


class MockSessionAuthLoggingView(LoggingMixin, APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("with session auth logging")

class MockCustomCheckLoggingWithLoggingMethodsFailView(LoggingMixin, APIView):
    """The expected behavior should be to save only the post request.
    Though, due to the improper `should_log` implementation both requests are saved.
    """

    logging_methods = ["POST"]

    def should_log(self, request, response):
        """
        Log only if response contains 'log'
        """
        return "log" in response.data

    def get(self, request):
        return Response("with logging")

    def post(self, request):
        return Response("with logging")