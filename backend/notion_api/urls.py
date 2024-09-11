from .views import notion_login, notion_callback, is_authenticated, test_cors
from django.urls import path



urlpatterns = [
    
    path("login/", notion_login),
    path("callback/", notion_callback ),
    path("is_authenticated/", is_authenticated),
    path('', test_cors)

]