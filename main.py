from tasks.parse import sum_vars
from celery import Celery
from celery.schedules import crontab

app = Celery('main')
app.config_from_object('core.celery_config')

app.conf.beat_schedule = {
    'scrape-task': {
        'task': 'tasks.parse.sum_vars',
        'schedule': crontab(minute="*/1"),
        'args': (3, 3),
    },
}

if __name__ == '__main__':
    app.start()
