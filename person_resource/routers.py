from rest_framework.routers import DefaultRouter


class OptionalSlashRouter(DefaultRouter):
    """
    Custom Router class to make the slash
    optional for all available routes
    """

    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = "/?"
