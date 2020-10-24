from app.api.api_v1.routers import account

route = [
    account.InstitutionViewSet,
    account.AccountOwnerViewSet,
    account.AccountViewSet,
]
