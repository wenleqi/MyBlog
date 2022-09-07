from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    """
    模块几类，所有模块继承这个类，并实现str魔法方法
    """
    created_time = models.DateTimeField(auto_now_add=True,help_text=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True,help_text=u'修改时间')

    class Meta:
        abstract = True
        ordering = ['-created_time']

    def __str__(self):
        raise Exception('没有数据显示')

class Topic(BaseModel):
    """博客主题"""
    title = models.CharField(max_length=200,help_text=u'主题')
    content = models.TextField(help_text=u'内容')
    is_online = models.BooleanField(default=True,help_text=u'话题是否在线')
    is_public = models.BooleanField(default=True,help_text=u'话题是否隐私')
    user = models.ForeignKey(to=User,to_field='id',on_delete=models.CASCADE,help_text=u'关联用户')

    def __str__(self):
        return '主题： %s 内容：%s ' % (self.title,self.content[:20])

class Comment(BaseModel):
    """评论"""
    comment = models.TextField(help_text=u'评论')
    up = models.IntegerField(default=0,help_text=u'支持')
    down = models.IntegerField(default=0,help_text=u'反对')
    topic = models.ForeignKey(to=Topic,to_field='id',on_delete=models.CASCADE,help_text=u'关联主题')
    user = models.ForeignKey(to=User,to_field='id',on_delete=models.CASCADE,help_text=u'关联用户')

    def __str__(self):
        return '用户: %s 评论: %s 赞 %s 踩 %s' % (self.user.username,self.comment[:20],self.up,self.down)