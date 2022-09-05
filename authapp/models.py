from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255, unique=True)
    userTypeId = models.ForeignKey(on_delete = models.SET_NULL, db_column = 'user_type_id', null=True, to='truesight.UserType')
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

