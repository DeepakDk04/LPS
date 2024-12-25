from django.db import models
from purchase.models import Purchase
from customer.models import Customer


class PointTransaction(models.Model):
    pointStatus = [
        ("no", "no"),
        ("partial", "partial"),
        ("yes", "yes"),
    ]
    points = models.PositiveSmallIntegerField()
    expireOn = models.DateField()
    createdOn = models.DateTimeField(auto_now_add=True)
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    isRedeemed = models.CharField(max_length=10, choices=pointStatus, default="no")
    balancePoints = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.points} - {self.customer}"
