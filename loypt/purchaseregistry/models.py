from django.db.models import (
    Model,
    CharField,
    FloatField,
    ForeignKey,
    SET_NULL,
    CASCADE,
    DateTimeField,
)
from catalogue.models import Catalogue
from consumer.models import Consumer
from vendor.models import Vendor


class PurchaseRegistry(Model):
    """
    Data Model to hold the incoming data for the consumer purchases.
    Used for analytics and logging.
    """

    purchaseRef = CharField(max_length=50)
    amount = FloatField()
    timeStamp = DateTimeField(auto_now_add=True)
    vendor = ForeignKey(Vendor, on_delete=SET_NULL, blank=True, null=True)
    orderCatlouge = ForeignKey(Catalogue, on_delete=SET_NULL, blank=True, null=True)
    consumer = ForeignKey(Consumer, on_delete=CASCADE)

    def __str__(self) -> str:
        return str(self.amount)
