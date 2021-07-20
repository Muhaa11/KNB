from django.db import models
from userlogin.models import CustomUser
import random


# Create your models here.

class Balance(models.Model):
    number = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __int__(self):
        return int(self.number)


    def save(self, *args, **kwargs):
        number_int = 500
        self.number = number_int
        super().save(*args, **kwargs)
