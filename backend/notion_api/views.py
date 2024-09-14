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
    NotionToken.objects.update_or_create(
        workspace_id=token['workspace_id'],
        defaults={
            'access_token': token['access_token'],
            'workspace_name': token['workspace_name'],
            'bot_id': token['bot_id'],
            'name': token['owner']['user']['name'],
        }
    )
    



    request.session.save()
    return redirect('http://localhost:5173/dashboard') 


def is_authenticated(request):
    print('checking for authentication')
    authentication = request.session.get("is_authenticated")
    print(authentication)
    return JsonResponse({'isAuthenticated': authentication})





def fetch_notion_pages(request):
    # Check if the user is authenticated
    if not request.session.get('is_authenticated'):
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    
        # Get the access token from the session
    token = request.session.get('oauth_token')
    access_token = token['access_token']
    headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"  # Ensure correct API version
    }

    url = "https://api.notion.com/v1/search"
    data = {
        "query": "",  # Search term, can be specific title/keywords
        "sort": {
            "direction": "ascending",
            "timestamp": "last_edited_time"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        pages = response.json()["results"]
        return JsonResponse({"pages": pages}, status=200)
    else:
        return JsonResponse({"error": "Failed to fetch pages"}, status=response.status_code)

