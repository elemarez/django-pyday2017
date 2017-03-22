from .models import Inscripcion
from django.forms import ModelForm


class InscripcionCreateForm(ModelForm):

    class Meta:
        model = Inscripcion
        fields = ('nombre_apellidos', 'nif', )
