from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group

from django.conf import settings
import sys

if hasattr(settings,"UNREGISTER_GROUP") and settings.UNREGISTER_GROUP == True:
    sys.stdout.write("\nUnregistering Group from admin because \"UNREGISTER_GROUP\" is True in settings")
    admin.site.unregister(Group)