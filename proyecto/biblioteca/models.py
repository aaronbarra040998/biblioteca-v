from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='foto/', blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)

    def __str__(self):
        return self.titulo