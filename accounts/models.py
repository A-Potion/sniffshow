from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
# Create your models here.

class CustomUser(models.Model):
    country = models.CharField(max_length=100)
