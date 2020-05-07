from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    mobile=models.CharField('手机号码',max_length=11,unique=True)
    #返回
    def __str__(self):
        # 如果不为空则返回用户名
        return self.username