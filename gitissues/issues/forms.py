from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields=('username','email','password',) 
