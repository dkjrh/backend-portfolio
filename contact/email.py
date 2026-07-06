from django.core.mail import send_mail
from django.conf import settings

def send_contact_email(name, email, message):
    subject = f"New message from {name}"
    body = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        ["okanyaemmanuel6@gmail.com"],
        fail_silently=False,
    )