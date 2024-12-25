from django.db import models
from django.contrib.auth.models import User, Group


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13, unique=True)
    pointsRemaining = models.SmallIntegerField(default=0)
    lastUpdatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()

    def save(self, **kwargs):
        customerGroup, created = Group.objects.get_or_create(name="Customer")
        if created:
            print("Customer Group Created")
        self.user.groups.add(customerGroup)
        return super().save(**kwargs)
