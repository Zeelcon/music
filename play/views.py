from django.http import StreamingHttpResponse
from index.models import *
import time
from django.shortcuts import render,redirect,reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import Http404
# Create your views here.

def playView(request, id):
    #热搜歌曲
    searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:1]
    #内容
    context = Song.objects.values('text').get(id=id)['text']
    #相关文章推荐
    type = Song.objects.values('label').get(id=id)['label']
    relevant = Dynamic.objects.select_related('song').filter(song__label=type).order_by('-plays').all()[:6]
    #歌曲信息
    songs = Song.objects.get(id=int(id))
    #播放列表
    play_list = request.session.get('play_list', [])
    exist = False
    if play_list:
        for i in play_list:
            if int(id) == i['id']:
                exist = True
    if exist ==False:
        play_list.append({'id':int(id), 'author':songs.author,'name':songs.name})
        request.session['play_list'] = play_list
        #歌曲

        #添加和播放次数
        #功能拓展：可食用Session实现每天只添加一次播放次数
        p = Dynamic.objects.filter(song_id=int(id)).first()
        plays = p.plays + 1 if p else 1
        Dynamic.objects.update_or_create(song_id=id , defaults={'plays':plays})

    if request.method == 'POST':
        text = request.POST.get('comment', '')
        if request.user.username:
            user = request.user.username
        else:
            user = '匿名用户'
        now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if text:
            comment = Comment()
            comment.text = text
            comment.user = user
            comment.date = now
            comment.song_id = id
            comment.save()
        return redirect(reverse('play', kwargs={'id': str(id)}))
    else:
        songs = Song.objects.filter(id=id).first()
        # 歌曲不存在，抛出404异常
        if not songs:
            raise Http404('歌曲不存在')
        c = Comment.objects.filter(song_id=id).order_by('-date')[:10]
        page = int(request.GET.get('page', 1))
        paginator = Paginator(c, 11)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
    return render(request, 'play.html', locals())

def downloadView(request, id):
    #添加下载次数
    p = Dynamic.objects.filter(song_id=int(id)).first()
    download = p.download + 1 if p else 1
    Dynamic.objects.update_or_create(song_id=id, defaults={'download': download})
    #读取文件内容
    #根据id查找歌曲信息
    songs = Song.objects.get(id=int(id))
    file = songs.file.url[1::]
    def file_iterator(file, chunk_size=512):
        with open(file, 'rb') as  f :
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:break
    #将文件内容写入StreamingHttpResponse对象
    #并以字节流方式返回给用户，实现文件下载
    f = str(id) + '.mp3'
    response = StreamingHttpResponse(file_iterator(file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition']='attachment;filename="%s"'%(f)
    return response

def commentView(request, id):
    #热搜歌曲
    searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:1]
    #点评内容的提交功能
    if request.method == 'POST':
        text = request.POST.get('comment', '')
        #如果用户处于登录状态，就是用用户名，否则使用匿名用户

