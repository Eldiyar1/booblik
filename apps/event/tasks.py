from celery import shared_task
from django.utils import timezone
from .models import Event


@shared_task
def publish_events():
    try:
        now = timezone.now()
        ready_to_publish = Event.objects.filter(publish_at__lte=now, is_published=False)
        for event in ready_to_publish:
            event.is_published = True
            event.save()
        return "ok"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
