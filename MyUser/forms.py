from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Member
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(max_length=100, required=True)
        last_name = forms.CharField(max_length=100, required=True)
        email = forms.CharField(max_length=100, required=True)
        date_joined = forms.CharField(max_length=100, required=True)

        model = User
        fields = ['username', 'email', 'password1', 'password2'
                  ]

