from django.db.models import Model, OneToOneField, CharField, CASCADE
from django.contrib.auth.models import User


class Vendor(Model):
    """
    Vendor Account
    """

    account = OneToOneField(User, on_delete=CASCADE)
    shortDescription = CharField(max_length=20)
    longDescription = CharField(max_length=60)
    addressDetails = CharField(max_length=100)
    pincode = CharField(max_length=6)
    state = CharField(max_length=15)
    contactNo = CharField(max_length=13)

    def __str__(self) -> str:
        return self.account.get_full_name() + f" ({self.account.get_username()})"
