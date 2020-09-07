from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views import View
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status
from django.http import HttpResponseForbidden
from django.http import HttpResponseForbidden
from django.http import JsonResponse

from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class APIAppAuthView(APIView):
    authentication_classes = [authentication.TokenAuthentication]    
    permission_classes = (permissions.IsAuthenticated,)    
    def dispatch(self, request, *args, **kwargs):
        if not request.user_in_group:
            return JsonResponse({}, status=status.HTTP_403_FORBIDDEN)
        else:
            return super(__class__,self).dispatch(request,*args, **kwargs) 

class AppAuthView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user_in_group:
            if not hasattr(settings,"REDIRECT_403_URL"):
                return HttpResponseForbidden()
            else:
                return redirect(reverse(settings.REDIRECT_403_URL)+f"?group_id={request.group_id}")
            
        else:
            return super(__class__,self).dispatch(request,*args, **kwargs) 
