from django.db import models

# Create your models here.
# 文章类别
class Label(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('类别标签', max_length=10)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '歌曲分类'
        verbose_name_plural = '歌曲分类'
        pass
    pass

#文章信息表
class Song(models.Model):
    id =models.AutoField('序号', primary_key=True)
    name = models.CharField('标题', max_length=50)
    author = models.CharField('作者',max_length=50)
    # time = models.CharField('时长', max_length=10)
    # album = models.CharField('专辑', max_length=50)
    # languages = models.CharField('语种', max_length=20)
    # type = models.CharField('类型', max_length=20)
    release = models.DateField('发布时间', auto_now=True)
    # img = models.FileField('文章封面', upload_to='Img/', default='Img/None/no_image.pig')
    text = models.TextField('内容', max_length=400,blank=False)
    file = models.FileField('歌曲文件', upload_to='songFile', default='songFile/None/no_image.pig')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, verbose_name='歌曲分类')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '文章信息'
        verbose_name = '文章信息'
        pass
    pass

#文章动态表
class Dynamic(models.Model):
    id = models.AutoField('序号', primary_key=True)
    plays = models.IntegerField('播放次数', default=0)
    search = models.IntegerField('搜素次数', default=0)
    download = models.IntegerField('下载次数', default=0)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='标题')

    class Meta:
        verbose_name = '文章动态'
        verbose_name_plural = '文章动态'
        pass
    pass

#文章点评表
class Comment(models.Model):
    id = models.AutoField('序号', primary_key=True)
    text = models.CharField('内容', max_length=500)
    user = models.CharField('用户', max_length=20)
    date = models.DateField('日期',auto_now=True)
    song = models.ForeignKey(Song,on_delete=models.CASCADE, verbose_name='歌名')

    class Meta:
        verbose_name_plural = '文章评论'
        verbose_name = '文章评论'


