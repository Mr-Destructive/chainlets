from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=64)

    class Meta:
        ordering = ['word',]
