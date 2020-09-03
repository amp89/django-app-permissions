from django.urls import resolve
from django.conf import settings

class AppAuthentication:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        app_name = view_func.__module__.split(".")[0].lower()
        # if not app_name.lower().startswith("django.contrib"):
        request.user_in_group = False
        if app_name in settings.DEVELOPER_INSTALLED_APPS:
            print(settings.DEVELOPER_INSTALLED_APPS)
            print(f" app name: {app_name}, request user: {request.user.username}")
            if (settings.ALLOW_ALL_SUPERUSER and request.user.is_superuser )or request.user.groups.filter(name=app_name).exists():
                request.user_in_group = True
        print(request.user_in_group)
        return None # Continue with view stuff
        