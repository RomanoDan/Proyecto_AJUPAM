from django import forms
from ranking.models import Jugador

categorias = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
    ]

class AgregarJugador(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    documento = forms.DecimalField(decimal_places=0,max_digits=8,error_messages={'max_digits':"El documento no debe superar los 8 digitos.","decimal_places":"El documento no puede tener decimales. ","unique":"El documento ingresado ya existe en la base de datos."})
    categoria = forms.ChoiceField(choices=categorias)

class BuscarJugador(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    categoria = forms.ChoiceField(choices=categorias, required=False)

class ModificarJugador(forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    foto = forms.ImageField(required=False,widget=forms.FileInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  # Solo si el jugador ya existe
            self.fields['fecha_creacion'].initial = self.instance.fecha_creacion  
    class Meta:
        model = Jugador
        fields = "__all__"
