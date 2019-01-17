from django.db import models


class Atracao(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 150)
    descricao = models.TextField()
    horario_func = models.CharField(max_length = 20)
    idade_minima = models.IntegerField()

    def __str__(self):
        return self.nome