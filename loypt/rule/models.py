from django.db import models
from vendor.models import Vendor


class Rule(models.Model):

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    isDerivePurchaseVal = models.BooleanField(default=False)
    purchasePercentage = models.PositiveSmallIntegerField(default=0)
    isPointLimit = models.BooleanField(default=False)
    pointLimit = models.PositiveSmallIntegerField(default=0)
    presetPoint = models.PositiveSmallIntegerField(default=0)
    daysToExpire = models.PositiveSmallIntegerField(default=100)
    isActive = models.BooleanField(default=True)
    ruleType = models.CharField(max_length=20, default="user-rule")
    isReuseable = models.BooleanField(default=True)
    createdBy = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)
    lastUpdatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
