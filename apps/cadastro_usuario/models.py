from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Empresas(models.Model):
    empresa = models.CharField(max_length=240)
    cnpj = models.CharField(max_length=240)



    def __str__(self):
        return self.empresa



class Usuario(models.Model):
    primeiro_nome = models.CharField(max_length=240, null=True, blank=True)
    segundo_nome = models.CharField(max_length=240, null=True, blank=True)
    email = models.EmailField(max_length=240)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.ManyToManyField(Empresas)



    def get_absolute_url(self):

        return reverse('create_usuario')


    def __str__(self):
        return self.primeiro_nome
