from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # Listado de eventos públicos (ListView)
    url(r'^evento/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detalle'),  # Detalle de un evento
    url(r'^evento/(?P<evento_id>[0-9]+)/inscribir/$', views.CreateView.as_view(), name='inscribir'),  #CreateView
    url(r'^inscripcion/(?P<pk>[0-9]+)/$', views.InscripcionDetailView.as_view(), name='inscripcion_detalle')
]