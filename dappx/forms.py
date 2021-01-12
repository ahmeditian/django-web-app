from dappx.models import UserFeedbackInfo
from dappx.models import UserProfileInfo
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class UserFeedbackInfoForm(forms.ModelForm):
    class Meta():
        model = UserFeedbackInfo
        fields = ('subject', 'message', 'attachment')
