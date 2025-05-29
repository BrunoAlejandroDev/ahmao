# catalogo/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) 
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)  # Define a data/hora quando o objeto é criado
    atualizado_em = models.DateTimeField(auto_now=True) # Define a data/hora sempre que o objeto é salvo

    def __str__(self):
        return self.nome