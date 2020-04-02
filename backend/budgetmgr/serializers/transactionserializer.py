from rest_framework import serializers
from budgetmgr.models.transaction import (
    ExpenseType
)


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
