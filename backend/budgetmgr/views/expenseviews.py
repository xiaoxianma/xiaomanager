from collections import defaultdict
from datetime import timedelta
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
        transactions = Transaction.objects.values('transaction_date').order_by('transaction_date').annotate(amount=Sum('amount'))
        transactions = self._zero_fill(transactions)
        return Response(transactions)

    def _zero_fill(self, transactions):
        if transactions.count() == 0: return
        last_date = transactions[0]['transaction_date']
        fill_transactions = []
        for transaction in transactions:
            curr_date = transaction['transaction_date']
            for delta in range(1, (curr_date - last_date).days):
                fill_date = last_date + timedelta(days=delta)
                fill_transactions.append({'transaction_date': fill_date, 'amount': 0})
            fill_transactions.append(transaction)
            last_date = curr_date
        return fill_transactions


class ExpenseMonthlyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        ret = defaultdict(list)
        query = Transaction.objects.annotate(date=TruncMonth('transaction_date')).values('date', category=F('expense_type__name')).order_by('date').annotate(amount=Sum('amount'))
        for item in query:
            year_month = str(item.pop('date'))[:7]
            ret[year_month].append(item)
        return Response(ret)

