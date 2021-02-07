from django.conf import settings
from django.db import models


class Bark(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=160)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.content
