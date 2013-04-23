'''
Created on 2013-4-13

@author: wwjiang
'''
from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.OneToOneField(User,verbose_name="用户")
    nicknme = models.CharField("昵称",max_length=30) 
    motto = models.CharField("格言",max_length=100) 
    pic = models.ImageField("头像",upload_to="image/user")
    pre_pic = models.ImageField("头像",upload_to="image/user")#切割前图片
    


class SocialModel(models.Model):#社交账号
    name = models.CharField("名称",max_length=30)
    user = models.ForeignKey(User,verbose_name="用户")
    

    