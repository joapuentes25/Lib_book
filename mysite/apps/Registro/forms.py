from django import forms
from django.forms import ModelForm
from .models import Libro, Profile
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import sys
from itertools import cycle

class LibroForm(ModelForm):

    titulo = forms.CharField(min_length=4, max_length=100)
    año = forms.IntegerField(min_value=1900)
    precio = forms.IntegerField(min_value=1)

    class Meta:
        model = Libro
        fields=['titulo', 'año', 'precio', 'autor', 'descripcion', 'tipo', 'imagen', 'user'] 
        exclude = ('user',)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['run','fecha_nac', 'telefono', 'region', 'ciudad']
        widgets={
            'fecha_nac': forms.SelectDateWidget(years=range(1990, 2021)),
            'run': forms.TextInput(attrs={'placeholder': 'Ej: 12345678-k'}),
        }
        labels={
            'fecha_nac':'Fecha de nacimiento'
        }

    def clean_run(self):

        run = self.cleaned_data['run']
        rut = run
        rut = rut.upper();
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]
    
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
    
        if str(res) == dv:
            return run
        elif dv=="K" and res==10:
            return run
        else:
            raise forms.ValidationError("Run incorrecto.")

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password1','password2']