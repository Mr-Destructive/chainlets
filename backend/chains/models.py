from django.db import models


class Chain(models.Model):
    prompt = models.CharField(max_length=256)
    words = models.TextField()

