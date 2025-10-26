

class BaseLogginMixin:
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        return super().finalize_response(self, request, response, *args, **kwargs)
