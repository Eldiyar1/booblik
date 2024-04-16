import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'publish-event-every-hour': {
        'task': 'apps.event.tasks.publish_events',
        "schedule": crontab(minute="*/1")
    },
}


@app.task()
def say_hello():
    print("Hello, World!")
