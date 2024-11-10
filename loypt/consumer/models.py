from django.db.models import Model, OneToOneField, CharField, IntegerField, CASCADE
from django.contrib.auth.models import User


class Consumer(Model):
    """
    Consumer Account
    """

    account = OneToOneField(User, on_delete=CASCADE)
    contactNo = CharField(max_length=13)
    secondaryContactNo = CharField(max_length=13, blank=True, null=True)
    pointBal = IntegerField(default=0)

    def __str__(self) -> str:
        return self.account.get_full_name() + f" ({self.account.get_username()})"
