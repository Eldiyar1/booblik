import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'manage-event-every-hour': {
        'task': 'apps.event.tasks.manage_events',
        'schedule': crontab(minute="*/1"),
        'args': ('publish',)
    },
    'remove-event-every-hour': {
        'task': 'apps.event.tasks.manage_events',
        'schedule': crontab(minute="*/1"),
        'args': ('remove',)
    },
    'update_product_prices_every_midnight': {
        'task': 'apps.menu.tasks.update_product_prices',
        # 'schedule': crontab(minute=0, hour=0)
        'schedule': crontab(minute="*/1")
    },
}


@app.task()
def say_hello():
    print("Hello, World!")
