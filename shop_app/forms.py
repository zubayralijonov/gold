from django import forms

from . models import UserAccount, User

from django.contrib.auth.forms import UserCreationForm

class UserAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name']