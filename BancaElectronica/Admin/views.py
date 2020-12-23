from django.shortcuts import render
from django.contrib import messages
from .forms import *
import MySQLdb
from  django.db.models import Q
# Create your views here.
db = MySQLdb.connect(host='localhost', user= 'Admin', password='Option65.la', db='BancaElectronica',port=7575, connect_timeout=5)
def admon (request):
    return render(request,'admon.html')

def empresa(request):
    global db
    form= Empresa()
    variables = {
        "form":form,
    }
    if request.method=="POST":
        form=Empresa(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='INSERT INTO usuario VALUES(null,\''+datos.get("Usuario")+'\',\''+datos.get("Password")+'\',\'Empresa\',\'0\')'
            c.execute(consulta)
            db.commit()
            flecha=c.lastrowid
            c.close()
            c=db.cursor()
            consulta='INSERT INTO empresa VALUES('+str(datos.get("nit"))+',\''+datos.get("Tipo_Empresa")+'\',\''+datos.get("nombre_empresa")+'\',\''+datos.get("nombre_comercial")+'\','
            consulta1='\''+datos.get("representante_legal")+'\',\''+datos.get("dirrecion")+'\','+str(datos.get("telefono_empresa"))+','+str(datos.get("telefono_representante"))+',\''+datos.get("email")+'\','+str(flecha)+')'
            consulta=consulta+consulta1
            c.execute(consulta)
            db.commit()
            c.close()
            messages.success(request, 'Cliente registrado con Exito')
            #nombre="Usuario Registrado"
            form=Empresa()
            #variables={"form":form,"mensaje":nombre}
    else:
        nombre="Usuario Ya registrado"
        variables={"form":form,}
    return render(request,'CreateCompany.html',variables)

def persona(request):
    form=Persona()
    variables={
        "form":form,
    }
    return render(request,'CreatePeopleClient.html',variables)
