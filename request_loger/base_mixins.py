import ipaddress

from django.utils.timezone import now


class BaseLogginMixin:

    def initial(self, request, *args, **kwargs):
        self.log = {"requested_at": now()}
        super().initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super(BaseLogginMixin, self).finalize_response(request, response, *args, **kwargs)
        self.log.update(
            {"remote_addr": self._get_ip_address(request),
             }
        )

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