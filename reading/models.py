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
        #类显示名称
        verbose_name = "读书会"
        #类名称复数形式
        verbose_name_plural = "读书会"

class ReadingNoteModel(ArticleModel):
    reading = models.ForeignKey(ReadingModel)
    class Meta:
        verbose_name = "读书笔记"
        verbose_name_plural = "读书笔记"
