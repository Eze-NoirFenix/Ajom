from django.urls import path

from proyecto_web_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.home, name='home'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('cookies_policy/', views.cookies_policy, name='cookies_policy'),
    path('aboutme/', views.aboutme, name='aboutme'),
]

if settings.DEBUG: #Dev Only

    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)