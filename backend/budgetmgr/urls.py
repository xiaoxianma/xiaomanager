from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from budgetmgr.views.accountviews import RewardViewSet, ListCurrentRewards


router = DefaultRouter()
router.register('reward', RewardViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    url('current-rewards/', ListCurrentRewards.as_view()),
]
