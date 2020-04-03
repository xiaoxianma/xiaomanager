from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from budgetmgr.views.accountviews import (
    AccountViewSet,
    RewardViewSet,
    ListCurrentRewards,
)
from budgetmgr.views.transactionviews import (
    ExpenseTypeViewSet,
    TransactionViewSet,
    MerchantViewSet,
)


router = DefaultRouter()
router.register('accounts', AccountViewSet)
router.register('rewards', RewardViewSet)
router.register('expense-types', ExpenseTypeViewSet)
router.register('transactions', TransactionViewSet)
router.register('merchants', MerchantViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url('current-rewards/', ListCurrentRewards.as_view()),
]
