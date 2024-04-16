from django.core.mail import send_mail
from django.core.cache import cache

from celery import shared_task


@shared_task
def send_otp_to_user_email(recipient_list, message):
    """Ставим задачу на отправку письма с одноразовым кодом."""
    subject = 'OTP code'
    from_email = 'cyourself@create.account'
    message = message
    recipient_list = recipient_list

    send_mail(subject, message, from_email, recipient_list)