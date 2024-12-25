from django.db import models
from campaign.models import Campaign
from customer.models import Customer
from rule.models import Rule
from vendor.models import Vendor


class Purchase(models.Model):
    """
    Read-Only Model & Should not be updated
    """

    # todo: to fix on delete default when the reference object deleted
    orderReference = models.CharField(max_length=30, default="999")
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        # todo: condition to validate the update
        super().save(**kwargs)

    def __str__(self):
        return f"{self.customer} - {self.amount}"
