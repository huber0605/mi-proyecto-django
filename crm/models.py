from django.db import models

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20, unique=True)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicios = models.ManyToManyField(Servicio)  # ✅ CAMBIADO
    fecha = models.DateField()
    hora = models.TimeField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Cita de {self.cliente.nombre} el {self.fecha}'

    def total_servicios(self):
        return sum(servicio.precio for servicio in self.servicios.all())





