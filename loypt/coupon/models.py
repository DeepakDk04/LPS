from django.db import models
from customer.models import Customer
from vendor.models import Vendor


class Coupon(models.Model):
    couponOrderNo = models.CharField(max_length=30, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=60)
    code = models.CharField(max_length=30)
    info = models.TextField()
    instruction = models.TextField()
    termsconditions = models.TextField()
    expiresOn = models.DateField()
    createdOn = models.DateTimeField(auto_now_add=True)
    pointsUsed = models.CharField(max_length=60)

    def __str__(self):
        return self.code
