from django.db.models import (
    Model,
    DateTimeField,
    FloatField,
    ForeignKey,
    OneToOneField,
    CASCADE,
    SET_NULL,
)
from consumer.models import Consumer
from vendor.models import Vendor
from purchaseregistry.models import PurchaseRegistry


class WalletPoint(Model):
    """
    Data Model to hold the wallet point detail for the consumer purchases.
    Points will be derived from Order Catalouge.
    """

    preBal = FloatField(default=0.0)
    newBal = FloatField(default=0.0)
    points = FloatField(default=0.0)
    purchase = OneToOneField(PurchaseRegistry, on_delete=CASCADE)
    expiry = DateTimeField()
    timeStamp = DateTimeField(auto_now_add=True)
    vendor = ForeignKey(Vendor, on_delete=SET_NULL, blank=True, null=True)
    consumer = ForeignKey(Consumer, on_delete=CASCADE)

    def __str__(self) -> str:
        return str(self.points)
