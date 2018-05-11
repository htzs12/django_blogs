from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name='昵称',default='小宝宝')
    email = models.CharField(max_length=100,verbose_name='邮箱')
    aboutme=models.TextField(max_length=100,verbose_name='个人介绍')
    address=models.CharField(max_length=100,verbose_name='地址')
    wechat=models.CharField(max_length=100,verbose_name='微信')
    image=models.ImageField(upload_to='image/%Y/%m',default='image/touxiang.jpg',max_length=100,verbose_name='头像')

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username


