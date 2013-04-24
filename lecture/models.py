'''
Created on 2013-4-12

@author: wwjiang
'''
from django.db import models
from org.models import OrgModel
from core.models import *
class LectureModel(ItemModel):
    class Meta:
        #类显示名称
        verbose_name = "讲座"
        #类名称复数形式
        verbose_name_plural = "讲座"
    

class OrgClassifyModel(ClassifyModel):
    
    pass
class ArticalClassifyModel(ClassifyModel):
    pass



class LectureNoteModel(ArticleModel):
    lecture = models.ForeignKey(LectureModel)
    class Meta:
        verbose_name = "讲座笔记"
        verbose_name_plural = "讲座笔记"