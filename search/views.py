from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from index.models import *


# Create your views here.
def searchView(request, page):
    if request.method == 'GET':
        #热搜歌曲
        searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:1]
        #获取搜索内容，如果kword为空。就查询全部歌曲
        kword = request.session.get('kword', '')
        if kword:
            # Q是SQL语句里的or语法
            songs = Song.objects.filter(Q(name__icontains=kword)|Q(singer=kword)).order_by('-release').all()
        else:
            songs = Song.objects.order_by('-release').all()[:50]
            #分页功能
        paginator = Paginator(songs, 5)
        try:
            pages = Paginator.page(page,1)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
            #添加歌曲搜索次数
        if kword:
            idList = Song.objects.filter(name__icontains=kword)
            for i in idList:
                #判断歌曲动态信息是否存在，若存在，则在原来的基础上+1
                dynamics = Dynamic.objects.filter(song_id=i.id)
                if dynamics:
                    dynamics.update(search=F('search') + 1)
                    #若动态信息不存在，则创建动态信息
                else:
                    dynamics = Dynamic(plays=0, search=1, download=0, song_id=i.id)
                    dynamics.save()
        return render(request, 'search.html', locals())
    else:
        #处理POST请求，并重定向搜索页面
        request.session['kword'] = request.GET.get('kword', '')
        return redirect(reverse('search', kwargs={'page':1}))
