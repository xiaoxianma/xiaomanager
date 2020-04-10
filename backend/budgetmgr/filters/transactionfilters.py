from django_filters import rest_framework as filters
from budgetmgr.models.transaction import Transaction


class TransactionFilter(filters.FilterSet):
    min_date = filters.IsoDateTimeFilter(field_name='transaction_date', lookup_expr='gte')
    max_date = filters.IsoDateTimeFilter(field_name='transaction_date', lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = ['transaction_date', 'min_date', 'max_date']

