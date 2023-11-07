from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    groups = None
    user_permissions=None
