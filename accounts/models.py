'''
Created on 2013-4-13

@author: wwjiang
'''
from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.OneToOneField(User,verbose_name="�û�")
    nicknme = models.CharField("�ǳ�",max_length=30) 
    motto = models.CharField("����",max_length=100) 
    pic = models.ImageField("ͷ��",upload_to="image/user")
    pre_pic = models.ImageField("ͷ��",upload_to="image/user")#�и�ǰͼƬ
    


class SocialModel(models.Model):#�罻�˺�
    name = models.CharField("����",max_length=30)
    user = models.ForeignKey(User,verbose_name="�û�")
    

    