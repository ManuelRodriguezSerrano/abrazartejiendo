from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Categorias(models.Model):
    nombre=models.CharField(max_length=100)
    def __string__(self):
        print(self.nombre)
        return self.nombre
class Noticias(models.Model):
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    img = models.ImageField(null=True,blank=True,upload_to='img/noticias',help_text="selecciona una imagen")
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado = models.DateField(blank=True,null=True)
    cateogrias = models.ManyToManyField('Categorias',related_name='Noticias')

    def publicarNoticias(self):
        self.publicado = datetime.now()
        self.save()

    def comentariosAprobados(self):
        return self.comentarios.filter(aprobados=True)

class Comentarios(models.Model):
    noticia = models.ForeignKey('Noticias',related_name='comentarios',on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cuerpo_comentario = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    aprobado = models.BooleanField(default=False)

    def aprobarComentarios(self):
        self.aprobado = True
        self.save()
        

    

    
    