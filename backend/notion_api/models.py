from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class NotionToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null = False, default = "")
    access_token = models.CharField(max_length=255, null = False, default = "")
    workspace_name = models.CharField(max_length=255, null= False, default = "")
    workspace_id = models.CharField(max_length=255, null= False, default = "")
    bot_id = models.CharField(max_length=255, null = True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}'s Notion Token"
        