import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .email import send_contact_email


@csrf_exempt
@api_view(["POST"])
def contact_view(request):
    # Read JSON data
    data = request.data

    if not data and request.body:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(
                {
                    "success": False,
                    "error": "Invalid JSON data."
                },
                status=400
            )

    # Get fields
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    # Validate
    if not name or not email or not message:
        return Response(
            {
                "success": False,
                "error": "All fields are required."
            },
            status=400
        )

    # Send email
    try:
        response = send_contact_email(name, email, message)

        return Response(
            {
                "success": True,
                "message": "Email sent successfully.",
                "response": response
            },
            status=200
        )

    except Exception as e:
        print("EMAIL ERROR:", str(e))

        return Response(
            {
                "success": False,
                "error": str(e)
            },
            status=500
        )