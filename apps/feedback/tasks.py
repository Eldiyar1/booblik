from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string

from apps.common.email_sender import EmailSender
from apps.geolocation.models import Location

email_sender = EmailSender()


@shared_task
def send_feedback_email(full_name, phone_number, comment, location_id):
    recipient_email = settings.EMAIL_HOST_USER
    try:
        location = Location.objects.get(id=location_id)
    except Location.DoesNotExist:
        return None
    context = {
        'full_name': full_name,
        'phone_number': phone_number,
        'comment': comment,
        'location_address': location.address,
    }
    email_body = render_to_string('feedback_email.html', context)
    subject = f"Обратная связь от {full_name}"
    email_sender.send_email(subject, email_body, recipient_email)
