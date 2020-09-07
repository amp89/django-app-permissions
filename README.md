# Django App Permissions

## What / Why
The purpose of this app is to automatically create a `Group` for each app, and manage authentication through that app by those `Group`s within the admin panel.

This is an Django app created to work with Django, DRF (Django Rest Framework), and Django DRF Advanced Token (Another Django app I wrote: https://pypi.org/project/django-drf-advanced-token/).

DRF Advanced Token is not necessary, but if it is not used there must be some middlewhere before Django App Permissions to add the user to the request object in order for this to work with DRF.

## How to Install

1.a Pip install everything you need.
  - New Project: `pip install --upgrade django-app-permissions`
  - Existing Project: `pip install --upgrade django djangorestframework django-app-permissions`

1.b (recommended) - Pip install Django DRF Advanced Token.  This package was tested using DRF Advanced Token, and I recommend using it: `pip install --upgrade django-drf-advanced-token`

2. Move the user installed apps (the one's you created with `python manage.py startapp`) to a new setting called `ACCESS_CONTROLLED_INSTALLED_APPS` *before* `INSTALLED_APPS` in the project `settings.py`
```python
ACCESS_CONTROLLED_INSTALLED_APPS = [
    'test_app_one',
    'test_app_two',
]
```

3. add ` + ACCESS_CONTROLLED_INSTALLED_APPS` to the end of the `INSTALLED_APPS` list in the project `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_advanced_token',
    'django_app_permissions'
] + ACCESS_CONTROLLED_INSTALLED_APPS
```

4. Add the middleware to `MIDDLEWARE` in the project `settings.py`:
```
MIDDLEWARE = [
    ...
    'django_app_permissions.middleware.auth.AppAuthentication',
    'drf_advanced_token.middleware.auth.ProcessToken', # Include this only if you are using Django DRF Advanced Token
]
```
## How to Use

If you want groups to be automatically created for each app, in your project `urls.py`, put this code:
```python
from django.core.management import call_command
call_command("resolve_app_groups")
```
This will automatically create a group for each app whenver Django starts. 

If you would rather do it manually, call `python manage.py resolve_app_groups`.


Django App Permissions comes with two views you can use.

`APIAppAuthView` for api views (extends A`rest_framework.views.APIView`), and `AppAuthView` for normal views (extends `django.views.View`).

Using these views within your app will lock that view to users that are part of that group.

Import them like this:
```
from django_app_permissions.views import APIAppAuthView
from django_app_permissions.views import AppAuthView
```

Use them like any view:
API (Extends rest_framework.views.APIView):
```python
class TestAPIView(APIAppAuthView):
    def get(self, request, *args, **kwargs):
        return Response({"hi":"bye"})
```

Regular View:
```python
class TestView(AppAuthView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hi")
```


### Options

#### Superusers can access all apps:
Add `ALLOW_ALL_SUPERUSER = True` to the project `settings.py` to allow superusers to access all apps without being explicitly added to the group.

#### Unregister `Group` from the admin page.
If you would like to remove `Groups` from the admin page, add `UNREGISTER_GROUP = True` to the project `settings.py`

#### Redirect on 403 in UI views
If you would like the user to be redirected somewhere, like an access request page, instead of getting a 403 AppAuthView, add `REDIRECT_403_URL` to the project `settings.py`.
`REDIRECT_403_URL` must be the **name** of a view that you would like the user to be redirected to.