from distutils.command.upload import upload
from django.db import models

class products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(max_length=500, verbose_name="Descripción")
    price = models.PositiveIntegerField(verbose_name="precio")
    img = models.ImageField(upload_to = 'static/img')
    brand = models.CharField(max_length=10, verbose_name="Marca")

    def __str__(self):
        return  self.name+"     " + self.brand+"    "+str(self.price)

class client(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=120)
    email = models.EmailField(max_length= 200, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return  self.firstName+" " + self.lastName+"    "+self.email

