'''
Created on 2013-4-20

@author: wwjiang
'''
from django.db import models
from django.contrib.auth.models import Group
from core.models import ArticleModel

class OrgModel(models.Models):
    #其图片轮显和侧边栏推广图可以放在特定路径下面，为每个组织设一个以名字命名的路径
    #基础资料
    group = models.OneToOneField(Group,verbose_name="协会名字")
    name = models.CharField("组织名称",max_length=30)
    pic = models.ImageField(upload_to="image/org","组织logo")
    purpose = models.TextField("组织宗旨")
    email = models.EmailField("组织邮箱")
    
    total_favor_number = models.IntegerField("总喜欢数")
    today_favor_number = models.IntegerField("今天喜欢数")
    total_click_number = models.IntegerField("总点击数")#其点击数为属于该org的所有页面的点击量
    today_click_number = models.IntegerField("今天点击数")
    
    def __unicode__(self):
        return self.name
    
class FriendLinkModel(models.Model):
    order = models.IntegerField("显示次序")
    name = models.CharField("名称",max_length=30)
    URL = models.URLField("链接地址",max_length=200)
    org = models.ForeignKey(OrgModel,verbose_name="推荐链接")
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ["order"]#升序排序
        
class MessageBoardModel(ArticleModel):
    org = models.ForeignKey(OrgModel)
    class Meta:
        verbose_name = "留言板"
        verbose_name_plural = "留言板"