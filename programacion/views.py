from django.shortcuts import render
from .models import *
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

