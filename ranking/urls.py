from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', rankingView, name='ranking'),
    path('.list', RankingList.as_view(), name='rankingList'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)