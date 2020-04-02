from django.contrib import admin
from budgetmgr.models import account, transaction


# Register your models here.
@admin.register(
    account.AccountType,
    account.Institution,
    account.AccountOwner,
    account.Account,
    account.RewardType,
    account.Reward,
)
class BudgetMgrAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(
    transaction.ExpenseType,
    transaction.Merchant,
    transaction.Transaction,
)
class BudgetMgrTransactAdmin(admin.ModelAdmin):
    pass
