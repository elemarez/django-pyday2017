from django.conf.urls import url
from . import views

# Espacio de nombres que será utilizado para identificar las urls que están definidas en este fichero.
# La identificación es app_name:name, por ejemplo usando events:index
app_name = 'events'

urlpatterns = [
    # Listado de eventos públicos (ListView)
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Detalle de un evento
    url(r'^evento/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detalle'),
    # Creación de una inscripción (formulario)
    url(r'^evento/(?P<evento_id>[0-9]+)/inscribir/$', views.CreateView.as_view(), name='inscribir'),
    # Detalle de una inscripción
    url(r'^inscripcion/(?P<pk>[0-9]+)/$', views.InscripcionDetailView.as_view(), name='inscripcion_detalle')
]
