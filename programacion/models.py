from django.db import models

# Create your models here.

class Horario(models.Model):
    horario= models.TimeField()
    def __str__(self):
        return self.horario
    
class Dia(models.Model):
    dia=models.DateField()
    def __str__(self):
        return self.dia
class Seleccion(models.Model):
    nombre=models.CharField(max_length=20)
    estadio=models.CharField(max_length=50)
    nivel_local=models.FloatField()
    nivel_visitante=models.FloatField()
    def __str__(self):
        return self.nombre
class Partidos(models.Model):
    Local=models.ForeignKey(Seleccion, related_name='local',on_delete=models.CASCADE)
    Visitante=models.ForeignKey(Seleccion, related_name='visitante', on_delete=models.CASCADE)
    horario=models.ForeignKey(Horario,related_name='hour',on_delete=models.CASCADE)
    dia=models.ForeignKey(Dia,related_name='day',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Local.nombre} VS {self.Visitante.nombre}"
    def c_local(self):
        p_local=(self.Local.nivel_local)
        p_visitante=(self.Visitante.nivel_visitante)
        probabilidad=p_local/(p_local+p_visitante)
        cuota_local=1/probabilidad
        return cuota_local
    def c_empate(self):
        p_local=(self.Local.nivel_local)
        p_visitante=(self.Visitante.nivel_visitante)
        probabilidad_empate=(p_local/(p_local+p_visitante))*(p_visitante/(p_local+p_visitante))
        cuota_empate=1/probabilidad_empate
        return cuota_empate
    def c_visitante(self):
        p_local=(self.Local.nivel_local)
        p_visitante=(self.Visitante.nivel_visitante)
        probabilidad_visita=p_visitante/(p_local+p_visitante)
        cuota_visitante=1/probabilidad_visita
        return cuota_visitante
    
class Posicion(models.Model):
    possicion=models.CharField(max_length=30)

class Jugadores(models.Model):
    nombres=models.CharField(max_length=30)
    posicion=models.ForeignKey(Posicion, related_name="position", on_delete=models.CASCADE)
    nacionalidad=models.ForeignKey(Seleccion, related_name="pais",on_delete=models.CASCADE)
    valor=models.IntegerField()
