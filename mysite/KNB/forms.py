from django import forms
from .models import Balance
from django.forms import fields
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django_cryptography.fields import encrypt


class Balance_form(forms.ModelForm):
    number = forms.CharField(label='Balance', help_text='')

    class Meta:
        model = Balance
        fields = ('number',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username',]

class Deposit_form(forms.ModelForm):
    d_amount = forms.IntegerField(label='Dbalance',help_text='Please enter your deposit amount')
    class Meta:
        model = Balance
        fields =('number',)