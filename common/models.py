from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nick = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(blank=True)
