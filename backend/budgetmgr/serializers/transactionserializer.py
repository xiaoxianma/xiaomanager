import json
from rest_framework import serializers
from django.core.serializers.json import DjangoJSONEncoder
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
        fields = '__all__'

    def create(self, validated_data):
        logger.info(f"creating transaction")
        logger.info(validated_data, indent=4, sort_keys=True, default=str)
        logger.info(json.dumps(validated_data, indent=4, cls=DjangoJSONEncoder))
        merchant = validated_data.pop('merchant')
        merchant_instance, created = Merchant.objects.get_or_create(**merchant)
        transaction_instance = Transaction.objects.create(**validated_data, merchant=merchant_instance)
        return transaction_instance
