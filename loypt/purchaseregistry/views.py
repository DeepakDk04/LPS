from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User, Group
from .models import PurchaseRegistry
from vendor.models import Vendor
from catalogue.models import Catalogue

from .serializers import PurchReg_CreateSerializer, IncomingApiDataSerializer

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
)


class IssuePointsAndCreatePurchaseView(CreateAPIView):
    """
    Issue loyalty point to consumer and
    Create purchase registry for the incoming api data
    """

    queryset = PurchaseRegistry.objects.all()
    serializer_class = PurchReg_CreateSerializer
    permission_classes = (IsAuthenticated,)

    def retriveVendor(self, authToken: str) -> Vendor | Response:
        """
        Validate the Vendor Credential and return Vendor Object if valid,
        otherwise, return 404 http response
        """
        # TODO: pesudo logic for auth token implementation
        authToken = "1"

        if not authToken:
            errorMessage = {"error": "You aren't authorized, missing credentials"}
            return Response(data=errorMessage, status=HTTP_401_UNAUTHORIZED)

        try:
            #  Retrive Vendor object using auth token - FIXME: need sanity check
            vendor = Vendor.objects.get(id=authToken)
        except Vendor.DoesNotExist:
            errorMessage = {"error": "You aren't authorized, incorrect credentials"}
            return Response(data=errorMessage, status=HTTP_404_NOT_FOUND)

        return vendor

    def retriveCatalogue(self, catalogueId: str) -> Catalogue | Response:
        """
        Return Order Catalouge object to be used to calculate LP,
        If no catalogue details given, Determine catalouge for this purchase and return Order Catalouge object
        otherwise, return 404 http response
        """
        if not catalogueId:
            # TODO: pesudo logic for determine catalogue implementation
            catalogueId = "1"

        try:
            #  Retrive Order Catalouge object using catalogueId
            catalogue = Catalogue.objects.get(id=catalogueId)
        except Catalogue.DoesNotExist:
            errorMessage = {"error": "incorrect catalogue, contact administrator"}
            return Response(data=errorMessage, status=HTTP_404_NOT_FOUND)

        return catalogue

    def calculatePoints(
        self, catalogue: Catalogue | None, vendor: Vendor | None, amount: float
    ) -> int:
        pass

    def post(self, request, *args, **kwargs):
        """
        overriding post method to tweek/validate incoming api data
        """
        # FIXME: implement custom serializer to validate incoming data from API route "IncomingApiDataSerializer"
        # TODO: refactor below methods - DRY

        # process auth token and get vendor details
        vendorId = request.headers.get("Authorization", None)
        vendor = self.retriveVendor(vendorId)

        # get order catalogue details
        catalogueId = request.data.get("catalogue", None)
        catalogue = self.retriveCatalogue(catalogueId)

        amount = request.data.get("amount", None)
        point = self.calculatePoints(catalogue, vendor, amount)

        # TODO: process the derivied values and issue points to consumer

        # calling super to continue purchase registry creation
        super().post(self, request, *args, **kwargs)
