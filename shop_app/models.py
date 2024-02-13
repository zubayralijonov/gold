from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    last_name = models.TextField(max_length=60)
    first_name = models.TextField(max_length=60)
