import os
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework import status
import requests
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from .ultils import check_notion_login

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
    if request.session.get('is_authenticated') == True:
        return redirect('http://localhost:5173/dashboard')
    notion = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = notion.authorization_url(AUTHORIZATION_BASE_URL)
    
    # Redirect the user to Notion's OAuth2 page
    return redirect(authorization_url)

def notion_callback(request):
    notion = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    token = notion.fetch_token(TOKEN_URL, authorization_response=request.build_absolute_uri(), client_secret=CLIENT_SECRET)

    # token, you can store it and use it to make API calls to Notion
    request.session['oauth_token'] = token
    request.session["is_authenticated"] = True
    request.session.save()
    return redirect('http://localhost:5173/dashboard') 


def is_authenticated(request):
    print('checking for authentication')
    authentication = request.session.get("is_authenticated")
    print(authentication)
    return JsonResponse({'isAuthenticated': authentication})

def test_cors(request):
    return JsonResponse({'message': "cors is here"})