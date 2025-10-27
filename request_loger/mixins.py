from .base_mixins import BaseLogginMixin
from .models import APIRequestLog


class LoggingMixin(BaseLogginMixin):
    def handle_log(self):

        APIRequestLog(**self.log).save()