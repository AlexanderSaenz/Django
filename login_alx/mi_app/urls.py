from django.urls import path
from . import views

urlpatterns = [
    path('', views.portafolio, name='portafolio'),
    path('hola/', views.hola_mundo),
    path('home/', views.home, name='home'),
]
