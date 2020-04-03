from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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
