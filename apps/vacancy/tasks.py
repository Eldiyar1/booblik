from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string

from apps.common.email_sender import EmailSender

email_sender = EmailSender()


@shared_task
def send_resume_email(email, full_name, phone_number, resume_content, resume_name, birth_date=None, gender=None):
    recipient_email = settings.EMAIL_HOST_USER
    context = {
        'full_name': full_name,
        'phone_number': phone_number,
        'email': email or "Не был указан",
        'birth_date': birth_date or "Не указана",
        'gender': gender or "Не указан",
    }
    email_body = render_to_string('send_resume_email.html', context)
    subject = f"Новое резюме от {full_name}"
    attachments = [(resume_name, resume_content)] if resume_content and resume_name else None
    email_sender.send_email(subject, email_body, recipient_email, attachments=attachments)
