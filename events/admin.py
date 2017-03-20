from django.contrib import admin
from .models import Evento, Inscripcion


# Modelo inscripción preparado para incorporar dentro de otro modelo en el admin
# Puede ser incorporado en modo TabularInline o StackedInline
class InscripcionInline(admin.TabularInline):
    # Modelo del que depende
    model = Inscripcion
    # Número de tuplas para rellenar, se pueden añadir más o eliminar directamente desde la ifaz, por defecto son 3
    extra = 2


class EventoAdmin(admin.ModelAdmin):
    # Campos que se muestran en la tabla de cada tupla. Se puede añadir campos no almacenados en BBDD,
    #  pero deben ser definidos en el modelo, por ejemplo 'es_hoy'
    list_display = ('nombre', 'fecha', 'es_publico', 'es_hoy', 'numero_inscripciones_libres')
    # Menú lateral de filtrado sobre las tuplas de la tabla
    list_filter = ('es_publico', 'fecha')
    # Modelo incorporado dentro del mismo modelo
    inlines = [InscripcionInline]
    # Listado de acciones sobre querysets definidas en el desplegable del Admin.
    actions = ['publicar']

    # Acción publicar de forma masiva
    def publicar(self, request, queryset):
        filas_actualizadas = queryset.update(es_publico=True)
        if filas_actualizadas == 1:
            message = "1 evento publicado"
        else:
            message = "%s eventos publicados" % filas_actualizadas
        self.message_user(request, "%s" % message)
    # Cadena que aparece en el desplegable
    publicar.short_description = "Hacer visibles (publicar) eventos"


class InscripcionAdmin(admin.ModelAdmin):
    # Estructura de campos agrupados al mostrar la información de un determinado objeto
    fieldsets = [
        ('Información personal', {'fields': ['nombre_apellidos', 'nif', 'correo']}),
        (None, {'fields': ['evento']})
    ]
    # Campos que se muestran en la tabla de cada tupla.
    list_display = ('nombre_apellidos', 'evento', 'creado_a')

# Si no se quiere sobreescribir nada del Admin por defecto, el register es: admin.site.register(Evento)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)
