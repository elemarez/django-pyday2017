from django.views import generic
from .forms import InscripcionCreateForm
from .models import Evento, Inscripcion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.shortcuts import get_object_or_404


# Create your views here.
class IndexView(generic.ListView):
    # template_name = 'events/evento_list.html'
    # context_object_name = 'object_list'

    def get_queryset(self):
        # Devuelve los eventos publicados por orden de fecha del evento
        return Evento.objects.filter(es_publico=True).order_by('-fecha')


class DetailView(generic.DetailView):
    model = Evento
    # template_name = 'events/evento_detail.html'


class CreateView(generic.CreateView):
    form_class = InscripcionCreateForm
    template_name = 'events/inscripcion_form.html'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['evento'] = get_object_or_404(Evento, id=self.kwargs.get('evento_id'))
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Guardar', css_class='btn btn-success'))
        form.helper.add_input(Button('cancel', 'Cancelar', css_class='btn btn-danger', onClick="history.back()"))
        return form

    def form_valid(self, form):
        form.instance.evento_id = self.kwargs.get('evento_id')
        return super(CreateView, self).form_valid(form)


class InscripcionDetailView(generic.DetailView):
    model = Inscripcion
