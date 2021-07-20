from userlogin.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import fields


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username',]