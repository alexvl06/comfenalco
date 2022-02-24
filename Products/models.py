from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(max_length=500, verbose_name="Descripción")
    price = models.PositiveIntegerField(verbose_name="precio")
    img = models.ImageField(upload_to = 'static/img')
    brand = models.CharField(max_length=10, verbose_name="Marca")

    def __str__(self):
        return  self.name+"     "+ self.brand+"    "+str(self.price)

class client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Nombre")
    image = models.ImageField(default = 'silueta.png', verbose_name="Imagen")

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now, verbose_name="Fecha")
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f'{self.user.username}: {self.content}'


class Solicitude(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests', verbose_name="Usuario")
    timestamp = models.DateTimeField(default=timezone.now, verbose_name="Fecha")
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='requests', verbose_name="Producto")
    quantity = models.PositiveBigIntegerField(verbose_name="Cantidad")
    pendiente = models.BooleanField(verbose_name="En proceso")

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f'Usuario {self.user}: Producto {self.product}'