from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.

class AccountManager(Base):
    def create_user(self. email, password=None, date_of_birth):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    USERNAME_FIELD = 'email'
