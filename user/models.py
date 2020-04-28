from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    qq = models.CharField('QQ号码', max_length=20)
    weChat = models.CharField('微信账号',max_length=20)
    mobile=models.CharField('手机号码',max_length=11,unique=True)
    #返回
    def __str__(self):
        if self.username:
            # 如果不为空则返回用户名
            return self.username
        else:
            # 如果用户名为空则返回不能为空的对象
            return self.username
