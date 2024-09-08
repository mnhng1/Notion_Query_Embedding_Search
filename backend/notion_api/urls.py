from .views import notion_login, notion_callback
from django.urls import path



urlpatterns = [
    
    path("login/", notion_login),
    path("callback/", notion_callback ),
    

]