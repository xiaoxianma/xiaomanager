from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from budgetmgr.views.accountviews import (
    RewardViewSet,
    ListCurrentRewards,
)
from budgetmgr.views.transactionviews import (
    ExpenseTypeViewSet,
    TransactionViewSet,
)


router = DefaultRouter()
router.register('rewards', RewardViewSet)
router.register('expense-types', ExpenseTypeViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url('current-rewards/', ListCurrentRewards.as_view()),
]
