# Definición de la estructura de las tablas en la BBDD
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Evento(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Título')
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

    # Nombre que identifica cada tupla de la tabla
    def __str__(self):
        return self.nombre

    # Método utilizado en el admin
    def es_hoy(self):
        return self.fecha.date() == timezone.now().date()
    # Por defecto, en admin no se ordenable este campo, aquí se especifica que campo ordena
    es_hoy.admin_order_field = 'fecha'
    # Si se indica que es boolean se le añade el widget en lugar de True o False
    es_hoy.boolean = True
    # verbose_name del método
    es_hoy.short_description = '¿Es hoy?'

    # Método utilizado en el admin
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
        # Orden por defecto al extraer las tuplas de la tabla
        ordering = ["creado_a"]
        # Plural del nombre público
        verbose_name_plural = "inscripciones"
        # Clave conjunta
        unique_together = (("nif", "evento"),)

    def get_absolute_url(self):
        return reverse('events:inscripcion_detalle', kwargs={'pk': self.pk})
