from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth

from budgetmgr.models.transaction import (
    Transaction,
)


class ExpenseDailyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(
            Transaction.objects
                .values('transaction_date')
                .order_by('transaction_date')
                .annotate(amount=Sum('amount'))
        )


class ExpenseMonthlyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(
            Transaction.objects
                .annotate(month=TruncMonth('transaction_date'))
                .values('month', category=F('expense_type__name'))
                .order_by('month')
                .annotate(amount=Sum('amount'))
        )

