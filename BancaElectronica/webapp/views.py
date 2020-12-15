from django.shortcuts import render

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
    return render(request,'index.html')