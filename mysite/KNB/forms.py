from django import forms
from .models import Balance
from django.forms import fields
from .models import CustomUser
from django_cryptography.fields import encrypt



class Withdrawform(forms.ModelForm):
    number = forms.IntegerField(label='balance',help_text='Please enter your deposit amount')
    class Meta:
        model = Balance
        fields = ('number',)



class DepositForm(forms.ModelForm):
    number = forms.IntegerField(label='balance',help_text='Please enter your deposit amount')
    class Meta:
        model = Balance
        fields = ('number',)