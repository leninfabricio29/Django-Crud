from django.urls import path
from cuenta import views

urlpatterns = [
    path('/registrar', views.registroCuenta, name='Registrar'),
    path('/listar', views.listarCuentas, name='Listar'),
  
]