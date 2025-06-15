from django.db import models
from catalogo.models import CraftType, Difficulty, Product

class Kit(models.Model):
    name = models.TextField()
    description = models.TextField()
    reference_month = models.DateField(null=True, blank=True) # Alterado para DateField
    craft_type = models.ForeignKey(CraftType, on_delete=models.PROTECT, related_name='kits')
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT, related_name='kits')
    products = models.ManyToManyField(Product, through='KitItem') # Relação Muitos-para-Muitos
    
    def __str__(self): return self.name

class KitItem(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()