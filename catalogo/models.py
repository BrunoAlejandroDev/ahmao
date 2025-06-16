'''
null=True: Diz ao banco de dados (PostgreSQL) que a coluna url_image pode armazenar valores NULL (nulos).
blank=True: Diz ao Django que, nos formulários (incluindo o do Admin), este campo pode ser deixado em branco.
'''

from django.db import models

class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    
    def __str__(self): return self.name

class CraftType(models.Model):
    name = models.TextField()
    
    def __str__(self): return self.name

class Difficulty(models.Model):
    name = models.TextField()
    
    def __str__(self): return self.name

class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    url_image = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self): return self.name