from celery import Celery

app = Celery('tasks')
app.config_from_object('core.celery_config')


@app.task()
def sum_vars(a, b):
    return a + b

