'''
Created on 2013-4-18

@author: wwjiang
'''
from django.db import models
from django.contrib.auth.models import User
from org.models import OrgModel

#分类
class ClassifyModel(models.Model):#多对一
    name = models.CharField("分类名称",max_length=30)
    class Meta:
        abstract = True

class ArticleClassifyModel(ClassifyModel):
    pass

class ItemClassifyModel(ClassifyModel):
    pass
      
class ItemModel(models.Model):
    name = models.CharField("名称",max_length=30)
    speaker = models.CharField("主讲人",mx_length=30)
    speaker_pic = models.ImageField(upload_to="image/item",blank=True)
    date = models.DateField("日期")
    time = models.CharField("时间")
    address = models.CharField("地址",max_length=60)
    fee = models.CharField("门票") #是否需要门票
    tags = models.CharField("标签",max_length=30) #至多三个且长度有限制
    classify = models.ForeignKey()
    detail = models.TextField("详细")
    source = models.ForeignKey(OrgModel,verbose_name="组织")
    user = models.ForeignKey(User,verbose_name="作者")
    hasRecord = models.BooleanField("有否录音")
    recordURL = models.URLField("录音地址",max_length=200,blank=True)
    state = (('unaudited','未审核'),('published','已发布'),('pending','挂起'))
    total_favor_number = models.IntegerField("总喜欢数")
    today_favor_number = models.IntegerField("今天喜欢数")
    total_click_number = models.IntegerField("总点击数")
    today_click_nmuber = models.IntegerField("今天点击数")
    class Meta:
        abstract = True #抽象基类
        ordering = ['-date','-time']#默认排序方式，时间降序

#文章
class ArticleModel(models.Model):
    #基本属性
    tittle = models.CharField("题目",max_length=30)
    content = models.TextField("正文")
    date = models.DateField("日期")
    time = models.TimeField("时间")
    state = (('unaudited','未审核'),('published','已发布'),('pending','挂起'))
    
    author = models.ForeignKey(User,verbose_name="作者")
    org = models.ForeignKey(OrgModel,verbose_name="社团")
    isOrigin = models.BooleanField("是否原创")
    classify = models.ForeignKey(ArticleClassifyModel,verbose_name="类别")
    
    total_favor_number = models.IntegerField("总喜欢数")
    today_favor_number = models.IntegerField("今天喜欢数")
    total_click_number = models.IntegerField("总点击数")
    today_click_number = models.IntegerField("今天点击数")
    class Meta:
        abstract = True
        
class TagModel(models.Model):#多对一
    name = models.CharField("标签名",max_length=10)
    article = models.ForeignKey(ArticleModel,verbose_name="文章")
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"
        
class StatModel(models.Model):
    click_number_today = models.IntegerField()
    click_number_today = models.IntegerField()
    
