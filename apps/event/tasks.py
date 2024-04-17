from celery import shared_task
from django.utils import timezone
from .models import Event

from django.core.exceptions import ValidationError


def handle_events(events, action):
    for event in events:
        if action == 'publish':
            event.is_published = True
            event.save()
        elif action == 'remove':
            event.delete()


@shared_task
def manage_events(action):
    try:
        now = timezone.now()
        if action == 'publish':
            events = Event.objects.filter(publish_at__lte=now, is_published=False)
        elif action == 'remove':
            events = Event.objects.filter(removal_at__lte=now, is_published=True)
        else:
            raise ValidationError('Invalid action. Action should be either "publish" or "remove".')

        handle_events(events, action)
        return "ok"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
