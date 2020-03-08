from django.contrib import admin
from budgetmgr.models import account, transaction


# Register your models here.
@admin.register(
    account.AccountType,
    account.Institution,
    account.Account,
    account.RewardType,
    account.Reward,
)
class BudgetMgrAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(
    transaction.ExpenseType,
)
class BudgetMgrTransactAdmin(admin.ModelAdmin):
    pass
