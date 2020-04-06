from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth

from budgetmgr.models.transaction import (
    Transaction,
)


class ExpenseDailyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(
            Transaction.objects.values('transaction_date').order_by('transaction_date').annotate(total_price=Sum('amount'))
        )


class ExpenseMonthlyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(
            Transaction.objects
                .annotate(month=TruncMonth('transaction_date'))
                .values('month')
                .order_by('month')
                .annotate(total_price=Sum('amount'))
        )

