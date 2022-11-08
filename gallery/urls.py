from django.urls import path
from . import views

urlpatterns = [

    path('galeria-vertical/', views.gallery_vertical, name='gallery-vertical'),
    path('galeria-horizontal/', views.gallery_widescreen, name='gallery-widescreen'),
    path('', views.gallery, name='gallery'),

]