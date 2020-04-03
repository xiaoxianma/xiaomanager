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


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant


class TransactionSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer

    class Meta:
        model = Transaction

    def create(self, validated_data):
        logger.info(f"creating transaction")
        logger.info(json.dumps(validated_data, indent=4))
        return Transaction.objects.create(**validated_data)
