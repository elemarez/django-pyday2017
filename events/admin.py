from django.contrib import admin
from .models import Evento, Inscripcion

class InscripcionInline(admin.TabularInline): #StackedInline):
    model = Inscripcion
    extra = 3

class EventoAdmin(admin.ModelAdmin):
    inlines = [InscripcionInline]
    list_display = ('nombre', 'fecha', 'es_publico', 'es_hoy', 'numero_inscripciones_libres')
    list_filter = ('es_publico', 'fecha')
    actions =['publicar']

    def publicar(self, request, queryset):
        filas_actualizadas = queryset.update(es_publico=True)
        if filas_actualizadas == 1:
            message = "1 evento publicado"
        else:
            message = "%s eventos publicados" % filas_actualizadas
        self.message_user(request, "%s" % message)

    publicar.short_description = "Hacer visibles (publicar) eventos"


class InscripcionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Información personal', {'fields':['nombre_apellidos', 'nif', 'correo']}),
        (None, {'fields': ['evento']})
    ]
    list_display = ('nombre_apellidos', 'evento', 'creado_a')

admin.site.register(Evento, EventoAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)