from django.db import models
from django.db.models.deletion import CASCADE
from cuenta.models import Cuenta
# Create your models here.

class Transaccion (models.Model):
    id = models.AutoField(primary_key=True)
    id_Cuenta = models.ForeignKey(Cuenta, on_delete=CASCADE)
    tipo_Transaccion = models.CharField(max_length=20)
    monto_Transaccion = models.DecimalField(max_digits=20 , decimal_places=2)
    fecha_Transaccion = models.DateField(auto_now=True)


    def __str__(self):
        return self.tipo_Transaccion