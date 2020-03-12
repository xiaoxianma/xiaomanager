from rest_framework import serializers
from budgetmgr.models.account import Reward


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
