from django.urls import path
from appBanco import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('/banca', views.banca, name='Banca'),
    path('/servicios', views.services, name='Servicios'),
    path('/informacion', views.information, name='Informacion'),
    path('/contactos', views.contact, name='Contactos'),
]
