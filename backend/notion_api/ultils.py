from django.shortcuts import redirect
from functools import wraps
import asyncio
from .models import NotionToken

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
    
def update_or_create_user_token(request):
    session_id = request.session.session_key

    NotionToken.objects.update_or_create(
        workspace_id=token['workspace_id'],
        defaults={
            'access_token': token['access_token'],
            'workspace_name': token['workspace_name'],
            'bot_id': token['bot_id'],
            'name': token['owner']['user']['name'],
        }
    )

    

def get_user_token(user):
    try:
        notion_token = NotionToken.objects.get(user=user)
        return notion_token.access_token
    except NotionToken.DoesNotExist:
        return None


def filter_blocks_by_keywords(blocks,keyword):
    filtered_blocks = []

    for block in blocks:
        block_type = block['type']
        content = block[block_type].get('text', [])
        text = "".join([text_elem['text']['content'] for text_elem in content])

        if any(keyword.lower() in text.lower() for keyword in keywords):
            filtered_blocks.append(block)
        
    return filtered_blocks