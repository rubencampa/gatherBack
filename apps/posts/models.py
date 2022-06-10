from distutils.command.upload import upload
from django.db import models
from apps.users.models import User

class Tema(models.Model):
    id = models.IntegerField('Id Tema', unique = True, primary_key=True)
    nombre = models.CharField('Tema nombre',max_length=50, unique = True)

class TipoPost(models.Model):
    id = models.IntegerField('Id Tipo Post', unique = True, primary_key=True)
    nombre = models.CharField('Tipo Post nombre',max_length=50, unique = True)

class Post(models.Model):
    id = models.IntegerField('Post Id', unique = True, primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tema = models.ForeignKey(Tema,on_delete=models.DO_NOTHING)
    titulo = models.CharField('Titulo Post', max_length=50)
    tipoPost = models.ForeignKey(TipoPost, on_delete=models.DO_NOTHING)
    contenido = models.CharField('Contenido del post',max_length=255, null=True, blank = True)
    rutaImgPost = models.ImageField('Imagen de perfil',upload_to="static/img/", null=True, blank = True)    
