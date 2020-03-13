from rest_framework import serializers
from budgetmgr.models.account import (
    Reward, Institution, AccountType, AccountOwner,
    Account, RewardType
)


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        exclude = ['id']


class AccountTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_name_display')

    class Meta:
        model = AccountType
        exclude = ['id']


class AccountOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountOwner
        exclude = ['id']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['id']


class RewardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        mode = RewardType
        exclude = ['id']


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        exclude = ['id']
        read_only_fields = ['account', 'reward_type']
        depth = 3

