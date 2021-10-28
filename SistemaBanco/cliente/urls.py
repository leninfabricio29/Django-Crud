from django.urls import path
from cliente import views

urlpatterns = [
    path('/registrar', views.registroCliente, name='Registrar'),
    path('/listar', views.listarClientes, name='Listar'),

]