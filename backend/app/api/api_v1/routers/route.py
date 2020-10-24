from app.api.api_v1.routers import account, transaction

route = [
    account.InstitutionViewSet,
    account.AccountOwnerViewSet,
    account.AccountViewSet,
    account.RewardTypeViewSet,
    account.RewardViewSet,
    transaction.ExpenseTypeViewSet,
    transaction.MerchantViewSet,
    transaction.Transaction,
]
