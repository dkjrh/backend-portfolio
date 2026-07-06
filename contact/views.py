from rest_framework.decorators import api_view
from rest_framework.response import Response
from .email import send_contact_email

@api_view(["POST"])
def contact_view(request):
    name = request.data.get("name")
    email = request.data.get("email")
    message = request.data.get("message")

    try:
        send_contact_email(name, email, message)
        return Response({"success": True, "message": "Email sent successfully"})
    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=500)