import json
from rest_framework import serializers
from budgetmgr.models.transaction import (
    ExpenseType,
    Transaction,
    Merchant,
)
from budgetmgr.tasks import create_transaction_entry
import logging

logger = logging.getLogger(__name__)


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
        fields = '__all__'


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer()
    expense_type_name = serializers.ReadOnlyField(source='expense_type.name')

    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'account', 'merchant', 'expense_type', 'expense_type_name',
                  'transaction_date', 'coupon', 'tags', 'notes', 'create_time')

    def create(self, validated_data):
        """
        "amount": 10.00,
        "account": 2,
        "expense_type": 1,
        "merchant": {
            "name": "hmart",
            "city": ""
        },
        "transaction_date": "2020-04-01",
        "coupon": null,
        "tags": [],
        "notes": ""
        """
        logger.info("forward transaction creation to celery")
        try:
            task_id = create_transaction_entry.delay(json.dumps(validated_data, indent=4, default=str))
        except Exception as e:
            logger.error(e)
            raise e
        logger.info(f"forward task={task_id} completes")

