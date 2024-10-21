from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    card_id_number=models.CharField(max_length=10)

