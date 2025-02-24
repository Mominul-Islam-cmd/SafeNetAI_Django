from django import forms
from django.contrib.auth.models import User
from login_app.models import UserInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Full Name',
            'email': 'Email Address',
            'password': 'Password',
           
        }
        help_texts = {
            'username': None,
        }


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('phone_number','institution','profile_pic')
        labels = {
            'phone_number': 'Mobile Number',
           
        }