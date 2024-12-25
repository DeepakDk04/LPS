from django.db import models
from django.contrib.auth.models import User, Group


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=60)
    address = models.CharField(max_length=120)
    pincode = models.CharField(max_length=6)
    state = models.CharField(max_length=20)
    contactNo = models.CharField(max_length=13)
    sharedKey = models.CharField(max_length=30, unique=True)
    apiKey = models.CharField(max_length=30, unique=True)
    lastUpdatedOn = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        vendorGroup, created = Group.objects.get_or_create(name="Vendor")
        if created:
            print("Vendor Group Created")
        self.user.groups.add(vendorGroup)
        return super().save(**kwargs)

    def __str__(self):
        return f"{self.user.get_username()} from {self.name}"
