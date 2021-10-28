from django.urls import path
from transaccion import views

urlpatterns = [
    path('/registrar', views.registroTransaccion, name='Registrar'),
    path('/listar', views.listarTransacciones, name='Listar'),

]