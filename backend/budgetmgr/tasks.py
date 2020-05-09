import json
from backend.celery import app
from budgetmgr.models.transaction import (
    Transaction,
    Merchant,
)
import logging

logger = logging.getLogger(__name__)


@app.task
def create_transaction_entry(serialized_data):
    logger.info("Celery Task: creating transaction entry")
    logger.info(f"creating transaction...")
    logger.info(serialized_data)
    data = json.loads(serialized_data)
    logger.info(f"decoded data={data}")
    merchant = data.pop('merchant')
    merchant_instance, created = Merchant.objects.get_or_create(**merchant)
    transaction_instance = Transaction.objects.create(
        **data,
        merchant=merchant_instance,
    )
    logger.info(f"Celery Task: transaction(id={transaction_instance.id}) is created!")
    return transaction_instance
