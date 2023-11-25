from django.db import models
from django.utils import timezone


# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField()
    telefone = models.IntegerField()
