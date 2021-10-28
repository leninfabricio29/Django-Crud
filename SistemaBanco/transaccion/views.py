from django.shortcuts import render
from .forms import TransaccionForm
from .models import Transaccion
from cuenta.models import Cuenta
# Create your views here.
def registroTransaccion(request):
    if request.method == 'GET': #si es por get, mostrar formulario
        form = TransaccionForm()
        contexto = {
        'form':form
    }
    else:
        form = TransaccionForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            print("Registro de Transaccion Valido")
    return render(request, 'registroTransaccion.html', contexto)

def listarTransacciones(request):
    transacciones = Transaccion.objects.all() #es un select all del modelo Persona, depende de lo q se retorne ahí traerá acá.
    contexto = {
        'transacciones': transacciones,
    }
    return render(request,'listadoTransacciones.html', contexto)