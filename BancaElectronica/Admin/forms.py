from django import forms
from .models import *

class Empresa(forms.Form):
    nit=forms.IntegerField(required=True, help_text='Campo Numerico')
    nombre_empresa=forms.CharField(required=True,max_length=50, help_text='Nombre de la empresa')
    nombre_comercial = forms.CharField(required=True, max_length=50, help_text='Nombre Comercial de la empresa')
    representante_legal = forms.CharField(required=True, max_length=75, help_text='Nombre Representante Legal')
    dirrecion = forms.CharField(required=True, max_length=250, help_text='Ingrese su dirrecion')
    telefono_empresa = forms.DecimalField(required=True,max_digits=8,decimal_places=0,help_text='Ingrese el numero telefonico')
    telefono_representante = forms.DecimalField(required=True,max_digits=8,decimal_places=0,help_text='Ingrese el numero telefonico')
    email = forms.EmailField(required=True,max_length=50,help_text='Ingrese su dirrecion de Correo')
    EmpresaTipo=(
        ('Sociedad Anonima','Sociedad Anonima'),
        ('Compania Limitada','Compania Limitada'),
        ('Empresa Individual','Empresa Individual'),
    )
    Tipo_Empresa= forms.ChoiceField(required=True,choices=EmpresaTipo)
    Usuario=forms.CharField(required=True,max_length=50,help_text='Requerido para Banca Electronica')
    Password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields=("nit","nombre_empresa","nombre_comercial","Tipo_Empresa","representante_legal","dirrecion","telefono_empresa","telefono_representante","email","Usuario","Password")

class  Persona(forms.Form):
    nit = forms.DecimalField(required=True, help_text="Campo Numerico",max_digits=8, decimal_places=0)
    cui = forms.DecimalField(required=True, help_text="Campo Numerico",max_digits=13, decimal_places=0)
    
#class Persona(forms.Form):