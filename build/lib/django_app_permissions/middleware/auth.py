from django.urls import resolve
from django.conf import settings
from django.contrib.auth.models import Group

class AppAuthentication:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        app_name = view_func.__module__.split(".")[0].lower()
        # if not app_name.lower().startswith("django.contrib"):
        request.user_in_group = False
        
        if app_name in settings.ACCESS_CONTROLLED_INSTALLED_APPS:
            if ((hasattr(settings,"ALLOW_ALL_SUPERUSER") and settings.ALLOW_ALL_SUPERUSER )and request.user.is_superuser ) \
                    or request.user.groups.filter(name=app_name).exists():
                request.user_in_group = True
            else:
                request.group_id = Group.objects.get(name=app_name).id
        return None # Continue with view stuff
        