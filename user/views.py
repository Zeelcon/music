from django.shortcuts import render,redirect,reverse
from .form import MyUserCreationForm
from django.db.models import Q
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .models import *
from index.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
#用户注册与登录
def loginView(request):
    user = MyUserCreationForm()
    #提交表单
    if request.method == 'POST':
        #判断表单提交使用户登录还是用户注册
        #用户登录
        if request.POST.get('loginUser', ''):
            u = request.POST.get('loginUser', '')
            p = request.POST.get('password', '')
            if MyUser.objects.filter(Q(mobile=u)|Q(username=u)):
                u1 =MyUser.objects.filter(Q(mobile=u)|Q(username=u)).first()
                if check_password(p, u1.password):
                    login(request, u1)
                    return redirect(reverse('comment', kwargs={'page': 1}))
                else:
                    tips = '密码错误'
            else:
                if u.errors.get('username', ''):
                    tips=u.errors.get('username','注册失败')
                else:
                    tips=u.errors.get('mobile','注册成功')
        return render(request, 'user.html', locals())
#用户中心
#设置用户登录限制
@login_required(login_url='/user/login.html')
def homeView(request, page):
    #热搜歌曲
    searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    #分页功能
    songs = request.session.get('play_list', [])
    paginator = Paginator(songs, 3)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'home.html', locals())

#退出登录
def logoutView(request):
    logout(request)
    return redirect('/')

