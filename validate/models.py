from django.db import models


class users(models.Model):
    username = models.TextField(max_length=50)
    password = models.CharField(max_length=50)
