from django.core.mail import EmailMessage


class EmailSender:
    def __init__(self, default_from_email='no-reply@yourdomain.com'):
        self.default_from_email = default_from_email

    def send_email(self, subject, body, recipient_email, from_email=None, reply_to=None, attachments=None):
        email_message = EmailMessage(
            subject=subject,
            body=body,
            from_email=from_email if from_email else self.default_from_email,
            to=[recipient_email]
        )
        if reply_to:
            email_message.reply_to = [reply_to]
        email_message.content_subtype = 'html'
        if attachments:
            for name, content in attachments:
                email_message.attach(name, content)
        email_message.send()
