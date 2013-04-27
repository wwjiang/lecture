'''
Created on 2013-4-18

@author: wwjiang
'''
from django.db import models
from django.contrib.auth.models import User
from org.models import OrgModel

#����
class ClassifyModel(models.Model):#���һ
    name = models.CharField("��������",max_length=30)
    class Meta:
        abstract = True

class ArticleClassifyModel(ClassifyModel):
    pass

class ItemClassifyModel(ClassifyModel):
    pass
      
class ItemModel(models.Model):
    name = models.CharField("����",max_length=30)
    speaker = models.CharField("������",mx_length=30)
    speaker_pic = models.ImageField(upload_to="image/item",blank=True)
    date = models.DateField("����")
    time = models.CharField("ʱ��")
    address = models.CharField("��ַ",max_length=60)
    fee = models.CharField("��Ʊ") #�Ƿ���Ҫ��Ʊ
    tags = models.CharField("��ǩ",max_length=30) #���������ҳ���������
    classify = models.ForeignKey()
    detail = models.TextField("��ϸ")
    source = models.ForeignKey(OrgModel,verbose_name="��֯")
    user = models.ForeignKey(User,verbose_name="����")
    hasRecord = models.BooleanField("�з�¼��")
    recordURL = models.URLField("¼����ַ",max_length=200,blank=True)
    state = (('unaudited','δ���'),('published','�ѷ���'),('pending','����'))
    total_favor_number = models.IntegerField("��ϲ����")
    today_favor_number = models.IntegerField("����ϲ����")
    total_click_number = models.IntegerField("�ܵ����")
    today_click_nmuber = models.IntegerField("��������")
    class Meta:
        abstract = True #�������
        ordering = ['-date','-time']#Ĭ������ʽ��ʱ�併��

#����
class ArticleModel(models.Model):
    #��������
    tittle = models.CharField("��Ŀ",max_length=30)
    content = models.TextField("����")
    date = models.DateField("����")
    time = models.TimeField("ʱ��")
    state = (('unaudited','δ���'),('published','�ѷ���'),('pending','����'))
    
    author = models.ForeignKey(User,verbose_name="����")
    org = models.ForeignKey(OrgModel,verbose_name="����")
    isOrigin = models.BooleanField("�Ƿ�ԭ��")
    classify = models.ForeignKey(ArticleClassifyModel,verbose_name="���")
    
    total_favor_number = models.IntegerField("��ϲ����")
    today_favor_number = models.IntegerField("����ϲ����")
    total_click_number = models.IntegerField("�ܵ����")
    today_click_number = models.IntegerField("��������")
    class Meta:
        abstract = True
        
class TagModel(models.Model):#���һ
    name = models.CharField("��ǩ��",max_length=10)
    article = models.ForeignKey(ArticleModel,verbose_name="����")
    class Meta:
        verbose_name = "��ǩ"
        verbose_name_plural = "��ǩ"
        
class StatModel(models.Model):
    click_number_today = models.IntegerField()
    click_number_today = models.IntegerField()
    
