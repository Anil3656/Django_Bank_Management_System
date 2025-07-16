from django import forms
from .models import Customer


class TransferForm(forms.Form):
    sender = forms.ModelChoiceField(queryset=Customer.objects.all())
    receiver = forms.ModelChoiceField(queryset=Customer.objects.all())
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=1)
    
    
    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']