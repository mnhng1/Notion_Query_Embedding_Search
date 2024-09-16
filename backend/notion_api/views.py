import os
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework import status
import requests
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import NotionToken, NotionPage
from .ultils import get_user_token,check_notion_login
from requests_oauthlib import OAuth2Session
import json
from django.conf import settings




from requests_oauthlib import OAuth2Session
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
load_dotenv()

CLIENT_ID = os.getenv("OAUTH_CLIENT_ID")
CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET")
REDIRECT_URI = 'http://localhost:8000/oauth/callback'
AUTHORIZATION_BASE_URL = 'https://api.notion.com/v1/oauth/authorize'
TOKEN_URL = 'https://api.notion.com/v1/oauth/token'
NOTION_AUTH_URL = "https://api.notion.com/v1/oauth/authorize?client_id=77626488-2026-45d6-bced-1f768e0d0f48&response_type=code&owner=user&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback"

def notion_login(request):
    
    notion = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = notion.authorization_url(AUTHORIZATION_BASE_URL)
    
    # Redirect the user to Notion's OAuth2 page
    return redirect(authorization_url)

def notion_callback(request):
    notion = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    token = notion.fetch_token(TOKEN_URL, authorization_response=request.build_absolute_uri(), client_secret=CLIENT_SECRET)

    #Storing token to database

    request.session['oauth_token'] = token
    request.session["is_authenticated"] = True

    # Create or update NotionToken
    
    

    if not request.session.exists(request.session.session_key):
            request.session.create()
        update_or_create_user_token(request.session.session_key, access_token=access_token, token_type= token_type, refresh_token= refresh_token, expires_in= expires_in)

    request.session.save()
    return redirect('http://localhost:5173/dashboard') 


def is_authenticated(request):
    print('checking for authentication')
    authentication = request.session.get("is_authenticated")
    print(authentication)
    return JsonResponse({'isAuthenticated': authentication})


def fetch_notion_pages(request):
    if not request.session.get('is_authenticated'):
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    token = request.session.get('oauth_token')
    access_token = token['access_token']
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Notion-Version": "2022-06-28"
    }

    url = "https://api.notion.com/v1/search"
    data = {
        "filter": {
            "value": "page",
            "property": "object"
        },
        "sort": {
            "direction": "descending",
            "timestamp": "last_edited_time"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        pages = response_data.get("pages", [])
        
        stored_count = 0
        for page in pages:
            if page['object'] == 'page':
                title = 'Untitled'
                if 'properties' in page:
                    title_property = page['properties'].get('Name', {}) or page['properties'].get('title', {})
                    if 'title' in title_property and title_property['title']:
                        title = title_property['title'][0].get('plain_text', 'Untitled')

                NotionPage.objects.update_or_create(
                    notion_id=page['id'],
                    defaults={
                        'title': title,
                        'content': page,
                    }
                )
                stored_count += 1

        return JsonResponse({"message": response_data})
    else:
        return JsonResponse({"error": "Failed to fetch pages", "status": response.status_code, "response": response.text}, status=response.status_code)


def fetch_important_sections(request):
    token = NotionToken.objects.get(user=request.user).access_token
    page_id = request.GET.get('page_id')
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28"
    }

    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        blocks = response.json().get('results', [])
        keywords = ['#important', '#summary']  # You can extend this to accept user input
        sections = ['heading_1', 'heading_2']
        filtered_blocks = []

        for block in blocks:
                block_type = block['type']
                if block_type in sections:
                    filtered_blocks.append(block)
                else:
                    content = block[block_type].get('text', [])
                    text = ''.join([elem['text']['content'] for elem in content])
                    if any(keyword in text for keyword in keywords):
                        filtered_blocks.append(block)

        return JsonResponse({'filtered_blocks': filtered_blocks})
    else:
        return JsonResponse({'error': 'Failed to fetch page content'}, status=400)