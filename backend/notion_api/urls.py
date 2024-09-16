from .views import notion_login, notion_callback, is_authenticated, fetch_notion_pages, fetch_important_sections
from django.urls import path



urlpatterns = [
    
    path("login/", notion_login),
    path("callback/", notion_callback ),
    path("is_authenticated/", is_authenticated),
    path('fetch-pages/', fetch_notion_pages, name='fetch_pages'),
    path('fetch-sections/', fetch_important_sections, name='fetch_sections'),
    

]