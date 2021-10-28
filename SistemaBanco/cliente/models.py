from django.db import models

# Create your models here.

class Cliente (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre