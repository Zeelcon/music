from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    #歌曲播放页
    path('<int:id>.html', playView, name='play'),
    # path('<int:id>.html', playerView, name='player'),
    #歌曲下载
    path('download/<int:id>.html', downloadView,name='download')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)