from django.shortcuts import render
from .models import *
# Create your views here.
def indexView(request):
    songDynamic =Dynamic.objects.select_related('song')
    #热搜
    searchs = songDynamic.order_by('-search').all()[:1]
    #分类
    labels = Label.objects.all()
    #热门
    popular = songDynamic.order_by('-plays').all()[:10]
    # 推荐
    recommend = Song.objects.order_by('-release').all()[:3]
    #热门搜索、热门
    downloads = songDynamic.order_by('-download').all()[:6]
    tabs = [searchs[:6],downloads]
    return render(request, 'index.html', locals())
