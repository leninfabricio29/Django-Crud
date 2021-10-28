from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        widgets={
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Ingrese el apellido'}),
            'cedula':forms.TextInput(attrs={'placeholder': 'Ingrese la cédula'}),
        }

