from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

# Create your views here.

from .forms import LoginForm,RegistrationForm,UserProfileForm,ChangePwdForm
from .models import UserInfo,UserProfile


def user_login(request):
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd=login_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('blog:blog_title'))
            else:
                return HttpResponseRedirect(reverse('account:login'))
        else:
            return HttpResponse('无效的登录')
    if request.method == 'GET':
        login_form=LoginForm()
        return render(request,'login.html',{'form':login_form})

def user_logout(request):
    if request.method=='GET':
        logout(request)
        return HttpResponseRedirect(reverse('blog:blog_title'))

def register(request):
    if request.method == 'POST':
        user_form=RegistrationForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            user_name=request.POST.get('username','')
            if User.objects.filter(username=user_name):
                return HttpResponse('用户名已存在~')
            else:
                new_user=user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                new_profile=userprofile_form.save(commit=False)
                new_profile.user=new_user
                new_profile.save()
                return HttpResponse('注册成功~')
        else:
            return HttpResponse('填写有误~')
    else:
        user_form=RegistrationForm()
        userprofile_form=UserProfileForm()
        return render(request,'register.html',{'form':user_form,'profile':userprofile_form})

def change_pwd(requset):
    pwd_form=ChangePwdForm(requset.POST)
    if pwd_form.is_valid():
        pwd1=requset.POST.get('password1','')
        pwd2=requset.POST.get('password2','')
        if pwd1 != pwd2:
            return HttpResponse('密码不一致~')
        user=requset.user
        user.password=make_password(pwd2)
        user.save()
        return HttpResponse('修改成功~')
    else:
        return render(requset, 'change_pwd.html', {'pwd_form':pwd_form})

@login_required(login_url='/account/login/')
def myself(request):
    user=User.objects.get(username=request.user.username)
    userprofile=UserProfile.objects.get(user=user)
    userinfo=UserInfo.objects.get(user=user)
    return render(request,'myself.html',{'user':user,'userprofile':userprofile,'userinfo':userinfo})

