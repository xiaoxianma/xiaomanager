from rest_framework import serializers
from budgetmgr.models.account import (
    Reward, Institution, AccountType, AccountOwner,
    Account, RewardType
)


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
        exclude = ['id']


class AccountTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_name_display')

    class Meta:
        model = AccountType
        fields = '__all__'
        exclude = ['id']


class AccountOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountOwner
        fields = '__all__'
        exclude = ['id']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['id']


class RewardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        mode = RewardType
        fields = '__all__'
        exclude = ['id']


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
        exclude = ['id']
        read_only_fields = ['account', 'reward_type']
        depth = 3
