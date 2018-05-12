from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
    username=forms.CharField(min_length=4,max_length=10)
    password=forms.CharField(min_length=6,max_length=20,widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','email')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('2次密码输入不一致~')
        return cd['password2']


class ChangePwdForm(forms.Form):
    password1=forms.CharField(required=True,min_length=5)
    password2=forms.CharField(required=True,min_length=5)

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['nick_name','email','wechat','aboutme','address']

class UploadImageForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['image']
