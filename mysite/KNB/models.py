from django.db import models
from userlogin.models import CustomUser


# Create your models here.

class Balance(models.Model):
    number = models.PositiveIntegerField(default = 500, null=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __int__(self):
        return int(self.number)


