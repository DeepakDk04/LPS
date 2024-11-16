from django.test import TestCase
from django.contrib.auth.models import User
from vendor.models import Vendor
from consumer.models import Consumer
from catalogue.models import Catalogue
from purchaseregistry.models import PurchaseRegistry
from walletpoint.models import WalletPoint

from Tests.modelFieldInputTestData import (
    user1TestData,
    user2TestData,
    vendor1TestData,
    consumer1TestData,
    catalogue1TestData,
    walletPoint1TestData,
    purchaseReg1TestData,
)


class ModelObjectCreatTest(TestCase):
    """
    Test Case for Data Model Object
    Models: User, Vendor, Consumer, Purchase Registry, Order Catalouge, Wallet Point
    """

    def setUp(self):
        """Model Object Initialization"""

        vendorUser = User.objects.create_user(**user1TestData)
        ven = Vendor.objects.create(account=vendorUser, **vendor1TestData)

        consumerUser = User.objects.create_user(**user2TestData)
        cons = Consumer.objects.create(account=consumerUser, **consumer1TestData)

        cat = Catalogue.objects.create(vendor=ven, **catalogue1TestData)

        purReg = PurchaseRegistry.objects.create(
            vendor=ven, orderCatlouge=cat, consumer=cons, **purchaseReg1TestData
        )

        WalletPoint.objects.create(
            purchase=purReg, vendor=ven, consumer=cons, **walletPoint1TestData
        )

    def test_object_creation(self):
        """test if model objects created successfully"""
        # User Object
        vendorUser = User.objects.get(username=user1TestData.get("username"))
        self.assertIsInstance(vendorUser, User, "check if vendor user created")

        consumerUser = User.objects.get(username=user2TestData.get("username"))
        self.assertIsInstance(consumerUser, User, "check if consumer user created")

        # Vendor Object
        ven = Vendor.objects.get(account=vendorUser)
        self.assertIsInstance(ven, Vendor, "check if vendor created")

        # Consumer Object
        con = Consumer.objects.get(account=consumerUser)
        self.assertIsInstance(con, Consumer, "check if consumer created")

        # Order Catalogue Object
        cat = Catalogue.objects.get(vendor=ven)
        self.assertIsInstance(cat, Catalogue, "check if order catalogue created")

        # Purchase Registry Object
        pruchReg1 = PurchaseRegistry.objects.get(consumer=con)
        self.assertIsInstance(
            pruchReg1, PurchaseRegistry, "check if purchase registry1 created"
        )
        pruchReg2 = PurchaseRegistry.objects.get(vendor=ven)
        self.assertIsInstance(
            pruchReg2, PurchaseRegistry, "check if purchase registry2 created"
        )
        pruchReg3 = PurchaseRegistry.objects.get(orderCatlouge=cat)
        self.assertIsInstance(
            pruchReg3, PurchaseRegistry, "check if purchase registry3 created"
        )
        self.assertEqual(
            pruchReg1,
            pruchReg2,
            "check if purchase registry taken using Consumer, Vendor are same",
        )
        self.assertEqual(
            pruchReg2,
            pruchReg3,
            "check if purchase registry taken using Vendor, Catalogue are same",
        )
        self.assertEqual(
            pruchReg3,
            pruchReg1,
            "check if purchase registry taken using Catalogue, Consumer are same",
        )

        # Wallet Point Object
        wallet1 = WalletPoint.objects.get(consumer=con)
        self.assertIsInstance(wallet1, WalletPoint, "check if wallet1 created")
        wallet2 = WalletPoint.objects.get(vendor=ven)
        self.assertIsInstance(wallet2, WalletPoint, "check if wallet2 created")
        self.assertEqual(
            wallet1, wallet2, "check if wallets taken using Consumer, Vendor are same"
        )
