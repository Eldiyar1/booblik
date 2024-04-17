from celery import shared_task
from django.template.loader import render_to_string

from apps.common.email_sender import EmailSender

email_sender = EmailSender()


@shared_task
def send_feedback_email(full_name, phone_number, comment):
    recipient_email = "mc.oks1@negmail.com"
    context = {
        'full_name': full_name,
        'phone_number': str(phone_number),
        'comment': comment,
    }
    email_body = render_to_string('feedback_email.html', context)
    subject = f"Обратная связь от {full_name}"
    email_sender.send_email(subject, email_body, recipient_email)
