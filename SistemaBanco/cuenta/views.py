from django.shortcuts import render
from .forms import CuentaForm
from .models import Cuenta
# Create your views here.
def registroCuenta(request):
    if request.method == 'GET': #si es por get, mostrar formulario
        form = CuentaForm()
        contexto = {
        'form':form
    }
    else:
        form = CuentaForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            print("Registro de Cuenta Valido")
    return render(request, 'registroCuenta.html', contexto)

def listarCuentas(request):
    cuentas = Cuenta.objects.all() #es un select all del modelo Persona, depende de lo q se retorne ahí traerá acá.
    contexto = {
        'cuentas':cuentas
    }
    return render(request,'listadoCuentas.html', contexto)