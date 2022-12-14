from django.db import models
from django.contrib.auth.models import User


class Newsletter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    mobile = models.TextField(blank=True, null=True)
    roll_number = models.TextField(blank=True, null=True)
    isSubscribed = models.BooleanField(default=False)

class Unregistered_subscriber(models.Model):
    email = models.EmailField(blank=True, null=True)



