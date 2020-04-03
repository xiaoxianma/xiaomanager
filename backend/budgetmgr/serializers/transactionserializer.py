import json
from rest_framework import serializers
from django.core.serializers.json import DjangoJSONEncoder
from budgetmgr.models.transaction import (
    ExpenseType,
    Transaction,
    Merchant,
)
from budgetmgr.models.account import (
    Account,
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
    merchant = MerchantSerializer()

    class Meta:
        model = Transaction
        # fields = ('id', 'amount', 'merchant', 'expense_type', 'transaction_date', 'coupon', 'tags', 'notes')
        fields = '__all__'

    def create(self, validated_data):
        """
        "amount": 10.00,
        "transaction_date": "2020-04-01",
        "account": 1,
        "expense_type": 1,
        "merchant": {"name": "hmart"},
        "coupon": null,
        "tags": [],
        "notes": ""
        """
        logger.info(f"creating transaction...")
        logger.info(json.dumps(validated_data, indent=4, cls=str))
        merchant = validated_data.pop('merchant')
        merchant_instance, created = Merchant.objects.get_or_create(**merchant)
        transaction_instance = Transaction.objects.create(
            **validated_data,
            merchant=merchant_instance,
        )
        return transaction_instance
