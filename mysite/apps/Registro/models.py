from django.db import models
from django.contrib.auth.models import User
# Create your models here.
TIPO_LIBRO = (
('Científico', 'Científico'),
('Literatura', 'Literatura'),
('Biografía', 'Biografía'),
('Cómic', 'Cómic')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField(max_length=12)
    fecha_nac = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=15)
    region = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    año = models.IntegerField(verbose_name="año")
    precio = models.IntegerField()
    autor = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    tipo = models.CharField(max_length=100, choices=TIPO_LIBRO)
    imagen = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    