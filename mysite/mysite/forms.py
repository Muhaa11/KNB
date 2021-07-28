from userlogin.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import fields


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')