from rest_framework.serializers import ModelSerializer, Serializer
from .models import PurchaseRegistry


class PurchReg_CreateSerializer(ModelSerializer):
    """
    Serializer for the Creating Purchase Registry
    """

    class Meta:
        model = PurchaseRegistry
        fields = ("purchaseRef", "amount", "vendor", "orderCatlouge", "consumer")

    # purchaseRef = CharField(max_length=50)
    # amount = FloatField()
    # timeStamp = DateTimeField(auto_now_add=True)
    # vendor = ForeignKey(Vendor, on_delete=SET_NULL, blank=True, null=True)
    # orderCatlouge = ForeignKey(Catalogue, on_delete=SET_NULL, blank=True, null=True)
    # consumer = ForeignKey(Consumer, on_delete=CASCADE)


class IncomingApiDataSerializer(Serializer):
    """
    Serializer for Incoming API Data TODO: implement incoming serializer
    """

    pass
