from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from budgetmgr.models.transaction import ExpenseType
from budgetmgr.serializers.transactionserializer import ExpenseTypeSerializer


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExpenseTypeSerializer
    queryset = ExpenseType.objects.all()
