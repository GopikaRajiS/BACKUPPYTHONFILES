from django.db import models

# Create your models here.

class Messages(models.Model):
    name = models.CharField(max_length=40,null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=12,null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)