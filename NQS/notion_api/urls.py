from .views import notion_login, handle_notion_callback
from django.urls import path


urlpatterns = [
    path("login/", notion_login),
    path("callback/", handle_notion_callback )

]