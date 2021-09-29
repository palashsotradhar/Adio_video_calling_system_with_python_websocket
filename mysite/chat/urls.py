from django.urls import path
from .views import  main_view,registration
from  django.contrib.auth.views import LoginView,LogoutView
app_name = "chat"

urlpatterns = [
    path('',main_view,name = 'main_view'),
    path('login/', LoginView.as_view(template_name='chat/login_system.html'), name="login"),
    path('registration/', registration, name="registration"),
]