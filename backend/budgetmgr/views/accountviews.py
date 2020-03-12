from rest_framework import viewsets
from budgetmgr.models.account import Reward
from budgetmgr.serializers.accountserializer import RewardSerializer
from rest_framework.permissions import IsAuthenticated


class RewardViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()
