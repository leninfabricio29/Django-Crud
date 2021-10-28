from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente
# Create your views here.
def registroCliente(request):
    if request.method == 'GET': 
        form = ClienteForm()
        contexto = {
        'form':form
    }
    else:
        form = ClienteForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            ("Registro Valido")
    return render(request, 'registroCliente.html', contexto)


def listarClientes(request):
    clientes = Cliente.objects.all() #es un select all del modelo Cliente
    contexto = {
        'clientes':clientes
    }
    return render(request,'listado.html', contexto)