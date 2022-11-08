from django.urls import path

from . import views

urlpatterns = [

    path('', views.store, name='store'),
    path('categoria/<int:category_id>/', views.category, name='category'),

]