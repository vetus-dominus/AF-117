# pylint: disable=no-member
""" Celery task """
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_message(rcptto, mailfrom, subject, message):
    """ Send email message """
    send_mail(
        subject=subject,
        message=message,
        from_email=mailfrom,
        recipient_list=[rcptto],
        fail_silently=False
    )
