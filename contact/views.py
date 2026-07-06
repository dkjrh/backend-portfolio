from rest_framework.decorators import api_view
from rest_framework.response import Response
from .email import send_contact_email

@api_view(["POST"])
def contact_view(request):
    name = request.data.get("name")
    email = request.data.get("email")
    message = request.data.get("message")

    if not name or not email or not message:
        return Response({"error": "All fields required"}, status=400)

    send_contact_email(name, email, message)

    return Response({"success": "Message sent successfully"})