import time
from django.core.cache import cache
from django_filters import rest_framework as filters
from celery.result import AsyncResult
from rest_framework import viewsets, status
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
from budgetmgr.filters.transactionfilters import (
    TransactionFilter,
)
from budgetmgr.utils.cache_key import CacheKey
import logging

logger = logging.getLogger(__name__)


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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionFilter

    def create(self, request, *args, **kwargs):
        logger.info("deleting daily&monthly expense cache...")
        cache.delete_many([CacheKey.DAILY_TRANSACTIONS, CacheKey.MONTHLY_TRANSACTIONS])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.create(serializer.validated_data)
        logger.info(f"celery task={task} is created")
        # syncing although this should be another task
        transaction_id = -1
        end = time.time() + 20
        while time.time() < end:
            task_result = AsyncResult(task.id)
            if task_result.ready():
                transaction_id = task_result.result
                break
            logger.info("waiting for transaction creation ready...")
            time.sleep(0.1)
        logger.info(f"transaction_id={transaction_id}")
        obj = Transaction.objects.get(id=transaction_id)
        data = serializer(obj)
        return Response(data, status=status.HTTP_201_CREATED)
