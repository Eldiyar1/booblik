from django.core.mail import EmailMessage


class EmailSender:
    """
    Класс для отправки электронных писем.

    Параметры:
    - default_from_email (str): Электронная почта по умолчанию, используемая в качестве отправителя.

    Методы:
    - send_email: Отправляет электронное письмо с указанными параметрами.
    """
    def __init__(self, default_from_email='no-reply@yourdomain.com'):
        self.default_from_email = default_from_email

    def send_email(self, subject, body, recipient_email, from_email=None, reply_to=None, attachments=None):
        """
        Параметры:
        - subject (str): Тема письма.
        - body (str): Тело письма.
        - recipient_email (str): Электронная почта получателя.
        - from_email (str, optional): Электронная почта отправителя. Если не указана, используется значение по умолчанию.
        - reply_to (str, optional): Электронная почта для ответа.
        - attachments (list, optional): Список вложений в формате (имя, содержимое).
        """
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

