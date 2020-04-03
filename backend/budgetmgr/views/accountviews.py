from datetime import datetime
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from budgetmgr.models.account import (
    Reward, Account,
)
from budgetmgr.serializers.accountserializer import (
    RewardSerializer, AccountSerializer
)


class RewardViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class ListCurrentRewards(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        now_time = datetime.now()
        rewards_queryset = Reward.objects.filter(
            Q(start_time__lte=now_time) &
            (Q(end_time__gte=now_time) | Q(end_time__isnull=True))
        )
        serializer = RewardSerializer(rewards_queryset, many=True)
        return Response(serializer.data)
