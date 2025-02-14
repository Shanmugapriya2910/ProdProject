import base64
import os
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from dotenv import load_dotenv

load_dotenv()

class BasicAuthMiddleware(MiddlewareMixin):
    VALID_USERNAME = os.getenv("AUTH_USERNAME", "admin")
    VALID_PASSWORD = os.getenv("AUTH_PASSWORD", "password")

    def process_request(self, request):
        if request.path == '/' or request.path.startswith("/admin/"):
            return None

        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Basic '):
            return JsonResponse({"error": "Missing or invalid Authorization header"}, status=401)


        encoded_credentials = auth_header.split(' ')[1]
        try:
            decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        except Exception:
            return JsonResponse({"error": "Invalid base64 encoding in Authorization header"}, status=401)


        try:
            username, password = decoded_credentials.split(':')
        except ValueError:
            return JsonResponse({"error": "Invalid credentials format"}, status=401)


        if username != self.VALID_USERNAME or password != self.VALID_PASSWORD:
            return JsonResponse({"error": "Invalid username or password"}, status=401)

        return None
