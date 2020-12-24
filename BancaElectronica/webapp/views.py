import MySQLdb
from django import forms
from webapp.forms import Login
from django.shortcuts import render
db = MySQLdb.connect(host='localhost', user= 'Admin', password='Option65.la', db='BancaElectronica',port=7575, connect_timeout=30)
# Create your views here.
def BancaPrincipal(request):
    return render(request,'Cuenta.html')
    
def EstadoCuenta(request):
    return render(request,'Estado.html')

def PlanillaProveedor(request):
    return render(request,'Planpro.html')

def Tercero(request):
    return render(request,'Terceros.html')

def Locales(request):
    return render(request,'Propias.html')
    
def CuentaActiva(request):
    return render(request,'suspender.html')

def CuentaSuspendida(request):
    return render(request,'Activar.html')

def Servicio(request):
    return render(request,'Servicios.html')

def PreCheques(request):
    return render(request,'ChequesPre.html')

def Prestamo(request):
    return render(request,'Prestamo.html')
    
def login(request):
    global db
    form=Login()
    var={
        "form":form,
    }
    if request.method=="POST":
        form=Login(data=request.POST)
        if form.is_valid():
            c=db.cursor()
            c.execute('SELECT * FROM usuario WHERE Usuario=%s and Pasword=%d',(form.get("Usuario"),form.get("Contraseña")))
            datos=c.fetchone()
            print(datos)

    return render(request,'index.html',var)