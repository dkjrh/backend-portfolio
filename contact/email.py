from django.core.mail import send_mail
from django.conf import settings

def send_contact_email(name, email, message):
    subject = f"New Contact Message from {name}"

    body = f"""
You received a new message:

Name: {name}
Email: {email}

Message:
{message}
"""

    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )