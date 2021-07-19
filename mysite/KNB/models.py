from django.db import models
from userlogin.models import CustomUser


# Create your models here.

class Balance(models.Model):
    number = models.PositiveIntegerField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __int__(self):
        return int(self.number)

    def save(self, *args, **kwargs):
        number = [500]
        number_balance = number
        
        number_int = "".join(str(item) for item in number_balance)
        self.number = number_int
        super().save(*args, **kwargs)
