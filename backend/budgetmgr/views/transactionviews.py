from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_countries import countries
from budgetmgr.models.transaction import (
    ExpenseType,
    Transaction,
    Merchant,
)
from budgetmgr.serializers.transactionserializer import (
    ExpenseTypeSerializer,
    TransactionSerializer,
    MerchantSerializer,
)


class ListCountries(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Return a list of all countries.
        """
        ret = []
        for k, v in dict(countries).items():
            ret.append({"id": k, "value": v})
        return Response(ret)


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExpenseTypeSerializer
    queryset = ExpenseType.objects.all()


class MerchantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MerchantSerializer
    queryset = Merchant.objects.all()


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
