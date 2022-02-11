from django.db import models


class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('preco', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('qtd_em_estoque')