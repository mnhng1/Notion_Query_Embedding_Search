from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class NotionToken(models.Model):
    user = models.CharField(max_length = 50, unique = True, null = True)
    name = models.CharField(max_length=255, null=False, default="")
    access_token = models.CharField(max_length=255, null=False, default="")
    workspace_name = models.CharField(max_length=255, null=False, default="")
    workspace_id = models.CharField(max_length=255, null=False, default="")
    bot_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"Notion Token for {self.name}"
        

class NotionPage(models.Model):
    notion_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    content = models.JSONField()
    vector = ArrayField(models.FloatField(), null=True, blank=True)
    cluster = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title