from django.shortcuts import redirect
from functools import wraps
import asyncio

def check_notion_login(request):
    # Handle CORS preflight request
    if request.method == "OPTIONS":
        response = JsonResponse({'message': 'CORS preflight'})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

    # Check if the user is authenticated via Notion
    if not request.session.get('is_authenticated'):
        # If not, redirect them to the Notion login page
        return redirect('http://localhost:8000/oauth/login')

    # Return None if authenticated
    return None
    


def get_user_token(user):
    try:
        notion_token = NotionToken.objects.get(user=user)
        return notion_token.access_token
    except NotionToken.DoesNotExist:
        return None