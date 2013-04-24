'''
Created on 2013-4-18

@author: wwjiang
'''
from django.db import models
from django.contrib.auth.models import User
from org.models import OrgModel
from core.models import *

class ReadingModel(ItemModel):
    class Meta:
        #����ʾ����
        verbose_name = "�����"
        #�����Ƹ�����ʽ
        verbose_name_plural = "�����"

class ReadingNoteModel(ArticleModel):
    reading = models.ForeignKey(ReadingModel)
    class Meta:
        verbose_name = "����ʼ�"
        verbose_name_plural = "����ʼ�"
