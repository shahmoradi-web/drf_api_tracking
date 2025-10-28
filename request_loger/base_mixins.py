import ipaddress

from django.utils.timezone import now
from .app_settings import app_settings


class BaseLogginMixin:

    def initial(self, request, *args, **kwargs):
        self.log = {"requested_at": now()}
        super().initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super(BaseLogginMixin, self).finalize_response(request, response, *args, **kwargs)
        user = self._get_user(request)

        self.log.update(
            {"remote_addr": self._get_ip_address(request),
             "view": self._get_view_name(request),
             "view_method": self._get_view_method(request),
             "path": self._get_path(request),
             "host": request.get_host(),
             "method": request.method,
             "user": user,
             "username_persistent": user.get_username() if user else "Anonymous",
             "response_ms": self._get_response_ms(),
             "status_code": response.status_code,
             }
        )
        self.handle_log()
        return response

    def handle_log(self):
        raise NotImplementedError


    def _get_ip_address(self, request):

        """Get the remote ip address the request was generated from."""

        ipaddr = request.META.get("HTTP_X_FORWARDED_FOR", None)
        if ipaddr:
            ipaddr = ipaddr.split(",")[0]
        else:
            ipaddr = request.META.get("REMOTE_ADDR", "").split(",")[0]

        possibles = (ipaddr.lstrip("[").split("]")[0], ipaddr.split(":")[0])

        for addr in possibles:
            try:
                return str(ipaddress.ip_address(addr))
            except ValueError:
                pass

        return ipaddr

    def _get_view_name(self, request):
        """Get view name."""
        method = request.method.lower()
        try:
            attributes = getattr(self, method)
            return f"{type(attributes.__self__).__module__}.{type(attributes.__self__).__name__}"

        except AttributeError:
            return None

    def _get_view_method(self, request):
        """Get view method."""
        if hasattr(self, "action"):
            return self.action or None
        return request.method.lower()

    def _get_user(self, request):
        """Get user."""
        user = request.user
        if user.is_anonymous:
            return None
        return user

    def _get_response_ms(self):
        """
        Get the duration of the request response cycle is milliseconds.
        In case of negative duration 0 is returned.
        """
        response_timedelta = now() - self.log["requested_at"]
        response_ms = int(response_timedelta.total_seconds() * 1000)
        return max(response_ms, 0)

    def _get_path(self, request):
        """Get the request path and truncate it"""
        return request.path[: app_settings.PATH_LENGTH]
