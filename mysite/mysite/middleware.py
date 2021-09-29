import re
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse
EX_URL = [re.compile(settings.LOGIN_URL)]
if hasattr(settings,'LOGIN_EX_URL'):
    EX_URL += [re.compile(url) for url in settings.LOGIN_EX_URL]
class LoginRedirectMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_view(self,request,view_func,view_args,view_kwargs):
        assert hasattr(request,'user')
        path = request.path_info
        #wait call ditachi
        #if not request.user.is_authenticated:
        #    if not any(url.match(path) for url in EX_URL):
        #        return redirect(settings.LOGIN_URL)
        url_is_exempt = any(url.match(path) for url in EX_URL)
        # if path == reverse('chat:logout'):
        #     logout(request)
        if path == reverse('chat:main_view') and not request.user.is_authenticated :
            return redirect(settings.LOGIN_URL)
        else:
            return None

