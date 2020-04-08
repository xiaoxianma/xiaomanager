from collections import defaultdict
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
        ret = defaultdict(list)
        query = Transaction.objects.annotate(date=TruncMonth('transaction_date')).values('date', category=F('expense_type__name')).order_by('date').annotate(amount=Sum('amount'))
        for item in query:
            year_month = str(item.pop('date'))[:7]
            ret[year_month].append(item)
        return Response(ret)

