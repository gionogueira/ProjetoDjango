from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=150)

    class Meta:
        db_table = "cliente"

