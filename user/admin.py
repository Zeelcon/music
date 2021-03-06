from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username','email','mobile']
    #在用户修改页面添加各个属性
    #将源码的UserAdmin.fieldsets转换成列表格式
    fieldsets = list(UserAdmin.fieldsets)
    #重写UserAdmin的fieldsets。
    fieldsets[1] = (_('Personal info'),{'fields':('email','mobile')})