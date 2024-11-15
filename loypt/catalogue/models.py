from django.db.models import (
    Model,
    CharField,
    IntegerField,
    BooleanField,
    FloatField,
    DateField,
    OneToOneField,
    CASCADE,
)

from vendor.models import Vendor


class Catalogue(Model):
    """
    Order Catalogue Rule Setup
    This will be used to dereive LP.
    """

    code = CharField(max_length=20, unique=True)
    IsPurchValApplicable = BooleanField(default=False)
    percentFromPurchVal = FloatField(blank=True, null=True)
    IsPreSetPointApplicable = BooleanField(default=False)
    preSetPoint = IntegerField(blank=True, null=True)
    IsPointCap = BooleanField(default=False)
    capPerOrder = IntegerField(blank=True, null=True)
    capPerConsumer = IntegerField(blank=True, null=True)
    capPerTimeline = IntegerField(blank=True, null=True)
    capTimeLine = DateField(blank=True, null=True)
    campaignName = CharField(max_length=20, default="New Campaign")
    campaignStartDate = DateField()
    campaignEndDate = DateField()
    vendor = OneToOneField(Vendor, on_delete=CASCADE)
    creationDate = DateField(auto_now_add=True)
    pointEffectiveDate = DateField()
    pointExpiryDate = DateField()
    IsCampaignCumulative = BooleanField(default=False)
    noOfTargetPoints = IntegerField(blank=True, null=True)
    noOfTargetCustomers = IntegerField(blank=True, null=True)
    pointsGenerated = IntegerField(default=0)
    customerReached = IntegerField(default=0)
    uniqueCustomerReached = IntegerField(default=0)

    def __str__(self) -> str:
        return (
            f"{self.code} ({self.vendor.account.get_full_name()}) - {self.campaignName}"
        )
