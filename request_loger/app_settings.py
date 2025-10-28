
class AppSettings(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        from django.conf import settings

        return getattr(settings, self.prefix + name, dflt)

    @property
    def PATH_LENGTH(self):
        """Maximum length of request path to log"""
        return self._setting("PATH_LENGTH", 200)

app_settings = AppSettings("DRF_TRACKING_")