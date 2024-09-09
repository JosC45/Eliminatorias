from django.urls import path
from . import views
urlpatterns = [
    path("inicio/",views.partidos,name="partidos"),
    path('seleccion/<int:p1>',views.seleccion,name="seleccion"),
    path('apuesta/',views.apuestas,name="apuestas"),
    path('valor/',views.calcular,name="calcular"),
    path('confirmacion/',views.confirmar,name="confirmar"),
    path("salir/",views.salir,name="salir")
]
