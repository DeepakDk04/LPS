from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13)
    pointsRemaining = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_username()
