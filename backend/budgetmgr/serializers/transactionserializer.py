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
    merchant = MerchantSerializer

    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        """
        'amount': 10.00,
        'transaction_date': '2020-04-01',
        'account': {'id': <id>},
        'expense_type': {'id': <id>},
        'merchant': {'name': <name>, 'city': null, 'country': null'},
        'coupon': null,
        'tags': [],
        'notes: '',
        """
        logger.info(f"creating transaction")
        logger.info(validated_data)
        logger.info(json.dumps(validated_data, indent=4, cls=DjangoJSONEncoder))

        account = validated_data.pop('account')
        account_id = int(account['id'])
        expense_type = validated_data.pop('expense_type')
        expense_type_id = int(expense_type['id'])
        merchant = validated_data.pop('merchant')
        merchant_instance, created = Merchant.objects.get_or_create(**merchant)

        transaction_instance = Transaction.objects.create(
            **validated_data,
            merchant=merchant_instance,
            account_id=account_id,
            expense_type_id=expense_type_id,
        )
        return transaction_instance
