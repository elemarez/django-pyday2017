from django.db import models

# Create your models here.
from django.utils import timezone
from django.urls import reverse

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField()
    es_publico =  models.BooleanField(default=False)
    localizacion = models.CharField(max_length=200)
    precio = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    maximo_inscripcion = models.IntegerField(help_text='Número máximo de inscripciones permitidas')
    web = models.URLField(max_length=100, blank=True, null=True)
    imagen = models.ImageField()
    creado_a = models.DateTimeField(auto_now_add=True)
    actualizado_a = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def es_hoy(self):
        return self.fecha.date() == timezone.now().date()
    es_hoy.admin_order_field = 'fecha'
    es_hoy.boolean = True
    es_hoy.short_description = '¿Es hoy?'

    def numero_inscripciones_libres(self):
        return self.maximo_inscripcion - self.inscritos.count()
    numero_inscripciones_libres.short_description = 'Plazas libres'


class Inscripcion(models.Model):
    nombre_apellidos = models.CharField(max_length=200)
    nif = models.CharField(max_length=9, )
    correo = models.EmailField(max_length=30)
    evento = models.ForeignKey(Evento, related_name='inscritos', )
    creado_a = models.DateTimeField(auto_now_add=True)
    actualizado_a = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_apellidos

    class Meta:
        ordering = ["creado_a"]
        verbose_name_plural = "inscripciones"
        unique_together = (("nif", "evento"),)

    def get_absolute_url(self):
        return reverse('events:inscripcion_detalle', kwargs={'pk': self.pk})