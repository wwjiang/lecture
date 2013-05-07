'''
Created on 2013-4-27

@author: wwjiang
'''

from django.db import models
from django.contrib.auth.models import User

class UserProfileModel(models.Model):
    user = models.OneToOneField(User,verbose_name="�û�")
    nicknme = models.CharField("�ǳ�",max_length=30) 
    motto = models.CharField("����",max_length=100) 
    pic = models.ImageField("ͷ��",upload_to="image/user")
    pre_pic = models.ImageField("ͷ��",upload_to="image/user")#�и�ǰͼƬ
    
    authorization_code = models.CharField()
    
    access_token = models.CharField()
    refresh_token = models.CharField()
    
    expires_in = models.IntegerField()
    
    class Meta:
        abstract=True
    
class RenrenUserProfile(UserProfileModel):
    user = models.ForeignKey(User,related_name="�����û�")
    
    scope = models.CharField()
    

class WeixinUserProfile(UserProfileModel):
    user = models.ForeignKey(User,related_name="΢���û�")

class QQUserProfile(UserProfileModel):
    user = models.ForeignKey(User,related_name="QQ�û�")

class DoubanUserProfile(UserProfileModel):
    user = models.ForeignKey(User,related_name="�����û�")
    douban_user_id = models.IntegerField()
    
    
