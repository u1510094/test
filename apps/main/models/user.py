from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None
    user_type = models.CharField(max_length=20, choices=None)

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
