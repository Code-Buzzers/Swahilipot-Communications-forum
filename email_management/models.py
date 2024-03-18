from django.db import models

from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)


class Template(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    