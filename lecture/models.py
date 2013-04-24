'''
Created on 2013-4-12

@author: wwjiang
'''
from django.db import models
from org.models import OrgModel
from core.models import *
class LectureModel(ItemModel):
    class Meta:
        #����ʾ����
        verbose_name = "����"
        #�����Ƹ�����ʽ
        verbose_name_plural = "����"
    

class OrgClassifyModel(ClassifyModel):
    
    pass
class ArticalClassifyModel(ClassifyModel):
    pass



class LectureNoteModel(ArticleModel):
    lecture = models.ForeignKey(LectureModel)
    class Meta:
        verbose_name = "�����ʼ�"
        verbose_name_plural = "�����ʼ�"