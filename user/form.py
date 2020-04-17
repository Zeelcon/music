from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django import forms
#表单模型
class MyUserCreationForm(UserCreationForm):
    #重写初始化方法
    #设置自定义字段
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs = {
                'class':'txt tabInput',
                'placeholder':'密码，4-16位数字、字母、符号（空格除外）'

            }
        )
        self.fields['pass']