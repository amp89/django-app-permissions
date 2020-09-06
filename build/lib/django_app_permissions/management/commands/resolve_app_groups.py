from django.core.management.base import BaseCommand, no_translations

from django.contrib.auth.models import Group

from django.conf import settings

import sys

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        sys.stdout.write("\nResolving app groups")
        app_list = [app_name.lower() for app_name in settings.ACCESS_CONTROLLED_INSTALLED_APPS]
        for app_name in app_list:
            created = Group.objects.get_or_create(name=app_name)
            sys.stdout.write(f"\n{app_name}, new={created}")
        
        sys.stdout.write("\n")