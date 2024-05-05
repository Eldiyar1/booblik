from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string

from apps.common.email_sender import EmailSender
from apps.filial.models import Filial

email_sender = EmailSender()


@shared_task
def send_feedback_email(full_name, phone_number, comment, location_id):
    recipient_email = settings.EMAIL_HOST_USER
    try:
        filial = Filial.objects.get(id=location_id)
    except Filial.DoesNotExist:
        return None
    context = {
        'full_name': full_name,
        'phone_number': phone_number,
        'comment': comment,
        'filial_address': filial.address,
    }
    email_body = render_to_string('feedback_email.html', context)
    subject = f"Обратная связь от {full_name}"
    email_sender.send_email(subject, email_body, recipient_email)
