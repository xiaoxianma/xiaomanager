import os
#####################################################################
# REDIS CONFIG
#####################################################################
REDIS_URL = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379')
BROKER_CONNECTION_MAX_RETRIES = os.environ.get('BROKER_CONNECTION_MAX_RETRIES', None)
BROKER_POOL_LIMIT = os.environ.get('BROKER_POOL_LIMIT', None)

#####################################################################
# CELERY CONFIG
#####################################################################
CELERY_BROKER_URL = REDIS_URL
#CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', REDIS_URL)
CELERY_REDIS_MAX_CONNECTIONS = os.environ.get('CELERY_REDIS_MAX_CONNECTIONS', 5)
CELERY_CONCURRENCY = os.environ.get('CELERYD_CONCURRENCY', 1)
