from django.db import models
from django.db.models.deletion import CASCADE
from cliente.models import Cliente
# Create your models here.
class Cuenta (models.Model):
    id = models.AutoField(primary_key=True)
    ahorros = "Ahorros"
    corriente = "Corriente"
    drop_Cuenta = [
        (ahorros, 'Ahorros'),
        (corriente, 'Corriente'),
        ]
    Tipo = models.CharField(max_length=20, choices=drop_Cuenta, default=ahorros)
    numero_Cuenta = models.CharField(max_length=20)
    id_Cliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    fecha_Creacion = models.DateField(auto_now_add=True)
    saldo_Dsiponible = models.DecimalField(max_digits=20 , decimal_places=2)

    def __str__(self):
        return self.numero_Cuenta