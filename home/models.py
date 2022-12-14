from django.db import models

class Contact(models.Model):
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)