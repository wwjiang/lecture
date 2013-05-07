'''
Created on 2013-4-27

@author: wwjiang
'''

from django.db import models
from django.contrib.auth.models import User

class UserProfileModel(models.Model):
    user = models.OneToOneField(User,verbose_name="用户")
    nicknme = models.CharField("昵称",max_length=30) 
    motto = models.CharField("格言",max_length=100) 
    pic = models.ImageField("头像",upload_to="image/user")
    pre_pic = models.ImageField("头像",upload_to="image/user")#切割前图片
    
    authorization_code = models.CharField()
    
    access_token = models.CharField()
    refresh_token = models.CharField()
    
    expires_in = models.IntegerField()
    
    class Meta:
        abstract=True
    
class RenrenUserProfile(UserProfileModel):
    user = models.ForeignKey(User,related_name="人人用户")
    
    scope = models.CharField()
    

class WeixinUserProfile(UserProfileModel):
    user = models.ForeignKey(User,related_name="微信用户")

class QQUserProfile(UserProfileModel):
    user = models.ForeignKey(User,related_name="QQ用户")

class DoubanUserProfile(UserProfileModel):
    user = models.ForeignKey(User,related_name="豆瓣用户")
    douban_user_id = models.IntegerField()
    
    
