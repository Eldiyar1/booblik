from celery import shared_task
from django.template.loader import render_to_string

from apps.common.email_sender import EmailSender

email_sender = EmailSender()


@shared_task
def send_resume_email(email, full_name, phone_number, resume_content, resume_name):
    recipient_email = "mc.oks1@negmail.com"
    context = {
        'full_name': full_name,
        'phone_number': str(phone_number),
        'email': email if email is not None else "Не был указан",
    }
    email_body = render_to_string('send_resume_email.html', context)
    subject = f"Новое резюме от {full_name}"
    attachments = [(resume_name, resume_content)] if resume_content and resume_name else None
    email_sender.send_email(subject, email_body, recipient_email, attachments=attachments)
