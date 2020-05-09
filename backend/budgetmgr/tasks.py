import json
from backend.celery import app
from budgetmgr.models.transaction import (
    Transaction,
    Merchant,
)
import logging

logger = logging.getLogger(__name__)


@app.task
def create_transaction_entry(validated_data):
    logger.info("Celery Task: creating transaction entry")
    logger.info(f"creating transaction...")
    logger.info(json.dumps(validated_data, indent=4, default=str))
    merchant = validated_data.pop('merchant')
    merchant_instance, created = Merchant.objects.get_or_create(**merchant)
    transaction_instance = Transaction.objects.create(
        **validated_data,
        merchant=merchant_instance,
    )
    logger.info(f"Celery Task: transaction(id={transaction_instance.id}) is created!")
    return transaction_instance
