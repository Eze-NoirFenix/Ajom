from django.urls import path
from . import views

urlpatterns = [

    path('', views.blog, name='blog'),
    path('categoria/<int:category_id>/', views.category, name='category'),

]