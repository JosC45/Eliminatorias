from django.urls import path
from . import views
urlpatterns = [
    path("inicio/",views.partidos,name="partidos"),
    path('seleccion/<int:p1>',views.seleccion,name="seleccion")
]
