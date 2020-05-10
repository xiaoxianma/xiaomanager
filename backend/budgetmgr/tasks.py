from backend.celery import app
from budgetmgr.models.transaction import (
    Transaction,
    Merchant,
)
import logging

logger = logging.getLogger(__name__)


@app.task
def create_transaction_entry(data):
    logger.info("Celery Task: creating transaction entry")
    logger.info(f"creating transaction...")
    logger.info(data)
    account_id = data.pop('account')
    expense_type_id = data.pop('expense_type')
    merchant = data.pop('merchant')
    merchant_instance, created = Merchant.objects.get_or_create(**merchant)
    transaction_instance = Transaction.objects.create(
        **data,
        merchant=merchant_instance,
        account_id=account_id,
        expense_type_id=expense_type_id
    )
    logger.info(f"Celery Task: transaction(id={transaction_instance.id}) is created!")
    return transaction_instance
