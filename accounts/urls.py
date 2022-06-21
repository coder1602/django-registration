from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' ,  views.home  , name="home"),
    path('register' , views.register_attempt , name="register_attempt"),
    path('accounts/login/' , views.login_attempt , name="login_attempt"),
    path('token' , views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' , views.error_page , name="error")
 
   
]