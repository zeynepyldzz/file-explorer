from django.db import models

class File(models.Model):
    #dosya adını temsil eden alan
    name = models.CharField(max_length=255)
    #dosya türünü temsil eden alan
    type = models.CharField(max_length=50)
    #dosya içeriğini temsil eden alan
    content = models.TextField(blank=True, null=True)
