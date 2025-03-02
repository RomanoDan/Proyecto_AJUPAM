from django.db import models

class Jugador(models.Model):
    categorias = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.DecimalField(decimal_places=0,max_digits=8,unique=True)
    categoria = models.IntegerField(choices=categorias,default="8")
    puntos = models.IntegerField(null=True,blank=True)
    participaciones = models.IntegerField(null=True,blank=True)
    foto = models.ImageField(null=True,blank=True, upload_to='fotosplayers')
    fecha_creacion = models.DateField(null=True,blank=True)

    def promedio(self):
        return self.puntos / self.participaciones if self.participaciones else 0

    def __str__(self):
        return f"{self.nombre} {self.apellido}"