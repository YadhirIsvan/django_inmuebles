from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from user_app.models import Account
class Empresa (models.Model): 
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Create your models here.
class Edificacion(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen =  models.CharField(max_length=900)
    activate =models.BooleanField(default=True)
    avg_calificacion = models.FloatField(default=0)
    number_calificacion = models.IntegerField(default=0)
    empresa  = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="empresa_nombre")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion
    
class Comentario(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=200, null = True)
    edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE, related_name="comentarios")
    active = models.BooleanField(default=True)
    create =models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.calificacion)