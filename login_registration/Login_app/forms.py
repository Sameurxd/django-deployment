from django import forms
#from Login_app import models
from django.contrib.auth.models import User
from Login_app.models import userInfo

# Default model of django
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


# Created Model and linked to django model
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = userInfo
        fields = ('facebook_id', 'profile_pic')
