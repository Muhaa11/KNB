from django import forms
from .models import Balance
from django.forms import fields
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django_cryptography.fields import encrypt


class Balance_form(forms.ModelForm):
    number = forms.CharField(label='Balance', help_text='Enter SMS verification code')

    class Meta:
        model = Balance
        fields = ('number',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username',]




