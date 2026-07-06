import resend
from django.conf import settings

resend.api_key = settings.RESEND_API_KEY


def send_contact_email(name, email, message):
    response = resend.Emails.send(
        {
            "from": "Portfolio <contact@yourdomain.com>",
            "to": ["okanyaemmanuel6@gmail.com"],
            "subject": f"New Portfolio Message from {name}",
            "text": f"""
Name: {name}
Email: {email}

Message:
{message}
""",
        }
    )

    print(response)

    return response