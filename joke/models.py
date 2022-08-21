import email
from django.db import models


# Create your models here.

class Email(models.Model):
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)


    def __str__(self):
        return self.email
