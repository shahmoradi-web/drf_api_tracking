from django.contrib import admin
from django.contrib.admin.models import LogEntry

from request_loger.models import APIRequestLog


# Register your models here.

@admin.register(APIRequestLog)
class  APIRequestLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "requested_at",
        "response_ms",
        "status_code",
        "user",
        "view_method",
        "path",
        "remote_addr",
        "host",
        "query_params",
    )