from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from budgetmgr.views.accountviews import RewardViewSet


router = DefaultRouter()
router.register('reward', RewardViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
