from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import AbstractUser
# # Create your models here.

class Bullet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bullet")
    num = models.IntegerField(default=30)

    def __str__(self):
        return self.owner.username


