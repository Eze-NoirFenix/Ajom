from django.urls import path
from .views import UserSignup, UserLogout, UserLogin

urlpatterns = [

    path('', UserSignup, name ='signup'),
    path('logout', UserLogout, name='logout'),
    path('login', UserLogin, name='login'),
]