from kombu import Exchange, Queue

from core.config import settings

BROKER_URL = settings.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = settings.CELERY_BACKEND_URL
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'UTC'
CELERY_DEFAULT_QUEUE = 'default'
CELERY_IMPORTS = ('tasks', )
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)
