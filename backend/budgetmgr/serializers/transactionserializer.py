import json
from rest_framework import serializers
from budgetmgr.models.transaction import (
    ExpenseType,
    Transaction,
    Merchant,
)
import logging

logger = logging.getLogger(__name__)


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
        exclude = ['id']


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        exclude = ['id']


class TransactionSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer

    class Meta:
        model = Transaction
        exclude = ['id']

    def create(self, validated_data):
        logger.info(f"creating transaction")
        logger.info(json.dumps(validated_data, indent=4))
        return Transaction.objects.create(**validated_data)
