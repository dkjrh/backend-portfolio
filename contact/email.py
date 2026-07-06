import resend

resend.api_key = "re_VyXotAo6_Di8uVk5ANVCabEKPUtXVevhm"

def send_contact_email(name, email, message):
    resend.Emails.send({
        "from": "yourdomain@resend.dev",
        "to": ["okanyaemmanuel6@gmail.com"],
        "subject": f"New Contact from {name}",
        "html": f"""
            <h3>New Contact Message</h3>
            <p><b>Name:</b> {name}</p>
            <p><b>Email:</b> {email}</p>
            <p><b>Message:</b><br>{message}</p>
        """
    })