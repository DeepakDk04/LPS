from django.db import models
from rule.models import Rule
from vendor.models import Vendor


class Campaign(models.Model):

    campaignStatus = [
        ("notready", "notready"),
        ("active", "active"),
        ("inactive", "inactive"),
        ("complete", "complete"),
        ("extend", "extend"),
    ]
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    activeRules = models.ManyToManyField(Rule, related_name="rulelist")
    rulesHistory = models.ManyToManyField(Rule, related_name="pastrule", blank=True)
    createdBy = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)
    lastUpdatedOn = models.DateTimeField(auto_now=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=10, choices=campaignStatus, default="notready")
    campaignType = models.CharField(max_length=20, default="user-campaign")
    isCumilative = models.BooleanField(default=False)
    targetPoints = models.PositiveIntegerField(default=1)
    targetPurchases = models.PositiveIntegerField(default=1)
    pointsGenerated = models.PositiveIntegerField(default=0)
    purchasesCount = models.PositiveIntegerField(default=0)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
