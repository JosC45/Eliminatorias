from django.shortcuts import redirect, render
from .models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


def partidos(request):
    # valor_local=Partidos.objects.values_list('Local__nivel_local',flat=True)
    # valor_visitante=Partidos.objects.values_list('Visitante__nivel_visitante',flat=True)
    partidos=Partidos.objects.all()
    horarios=Horario.objects.all()
    # def probabilidad(v_local,v_visitante):
    #     cl=v_local*v_local/v_visitante
    #     ce=(v_local+v_local)/v_visitante
    #     cv=(v_visitante*v_visitante)/v_local
    #     tupla=(cl,ce,cv)
    #     return tupla
    # nuevalista=[]
    # for i in range(len(valor_local)):
    #     nuevalista.append(probabilidad(valor_local[i],valor_visitante[i]))
    
    return render(request,'inicio.html',{'partidos':partidos,'horario':horarios})


def seleccion(request,p1):
    seleccion=Jugadores.objects.select_related('nacionalidad').filter(nacionalidad=p1)
    return render(request,'seleccion.html',{'seleccion':seleccion,'p1':p1})

def cambio(valor):
    valor=valor.replace(",",".")
    return float(valor)

def apuestas(request):
    if request.method=='POST':
        valores_seleccionados=request.POST.getlist("valores")
        
        apuestas=[cambio(valor) for valor in valores_seleccionados]
        #print(apuestas) 
        objetos=Partidos.objects.all()
        #print(objetos[1].c_local())
        objetos_filtrados = []
        for objeto in objetos:
            for apuesta in apuestas:
                if objeto.c_local()==apuesta or objeto.c_empate()==apuesta or objeto.c_visitante()==apuesta:
                    objetos_filtrados.append(objeto)
        #print(objetos_filtrados)
        # objetos_fil=list(zip(objetos_filtrados,apuestas))
        # print(objetos_fil)
        #print(apuestas)
        apus=1
        for apues in apuestas:
            apus*=apues
        #print(apus)
    return render(request,'apuestas.html',{'partido':objetos_filtrados,'apuestas':apuestas,'apus':apus})

@require_http_methods(["GET", "POST"])
def calcular(request):
    ganancias = None
    cuota = None
    cantidad = None
    
    if request.method == 'POST':
        cuota = request.POST.get('cuota')
        cantidad = request.POST.get('cantidad')
        
        try:
            cuotas = cambio(cuota)
            cantidades = cambio(cantidad)
            ganancias = cuotas * cantidades
        except ValueError:
            # Manejar el error si no se puede convertir a float
            ganancias = "Error: Por favor, ingrese valores numéricos válidos."
    print(cuotas)
    print(cantidades)
    print(ganancias)
    return render(request,'apuestas.html',{'ganancia':ganancias,'cuota':cuotas,'cantidad':cantidades})
@login_required 
def confirmar(request):
    if request.method=="POST":
        cuota=cambio(request.POST.get("cuota")) 
        cantidad=cambio(request.POST.get("cantidad"))
        ganancia=cambio(request.POST.get("ganancia"))
        usuar=request.user.id      
        usuario=User.objects.get(id=usuar)
        print(cuota,cantidad,ganancia,usuario)
        if cuota and cantidad and ganancia:
            nueva_boleta=Boleta(
                cuota =cuota,
                cantidad =cantidad,
                total =ganancia,
                id_usuario =usuario)
            nueva_boleta.save()
    return render(request,'confirmacion.html')
def salir(request):
    logout(request)
    return redirect("partidos")