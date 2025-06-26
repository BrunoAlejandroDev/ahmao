from django.db import models
from contas.models import User, Address
from catalogo.models import Difficulty, CraftType
from kits.models import Kit

class Plan(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.IntegerField() # Ex: 30 para mensal
    is_activate = models.BooleanField(default=True)
    def __str__(self): return self.name

class Subscription(models.Model):
    STATUS_CHOICES = [('active', 'Ativa'), ('paused', 'Pausada'), ('canceled', 'Cancelada')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name='subscriptions')
    start_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
    craft_type = models.ForeignKey(CraftType, on_delete=models.PROTECT)
    def __str__(self): return f"{self.user.username} - {self.plan.name}"

class Payment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.TextField()
    status = models.TextField()

class Shipment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='shipments')
    kit = models.ForeignKey(Kit, on_delete=models.PROTECT, related_name='shipments')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='shipments')
    shipment_date = models.DateField()
    tracking_code = models.TextField(null=True, blank=True)
    status = models.TextField()