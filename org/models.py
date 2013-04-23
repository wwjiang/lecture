'''
Created on 2013-4-20

@author: wwjiang
'''
from django.db import models
from django.contrib.auth.models import Group
from core.models import ArticleModel

class OrgModel(models.Models):
    #��ͼƬ���ԺͲ�����ƹ�ͼ���Է����ض�·�����棬Ϊÿ����֯��һ��������������·��
    #��������
    group = models.OneToOneField(Group,verbose_name="Э������")
    name = models.CharField("��֯����",max_length=30)
    pic = models.ImageField(upload_to="image/org","��֯logo")
    purpose = models.TextField("��֯��ּ")
    email = models.EmailField("��֯����")
    
    total_favor_number = models.IntegerField("��ϲ����")
    today_favor_number = models.IntegerField("����ϲ����")
    total_click_number = models.IntegerField("�ܵ����")#������Ϊ���ڸ�org������ҳ��ĵ����
    today_click_number = models.IntegerField("��������")
    
    def __unicode__(self):
        return self.name
    
class FriendLinkModel(models.Model):
    order = models.IntegerField("��ʾ����")
    name = models.CharField("����",max_length=30)
    URL = models.URLField("���ӵ�ַ",max_length=200)
    org = models.ForeignKey(OrgModel,verbose_name="�Ƽ�����")
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ["order"]#��������
        
class MessageBoardModel(ArticleModel):
    org = models.ForeignKey(OrgModel)
    class Meta:
        verbose_name = "���԰�"
        verbose_name_plural = "���԰�"