'''
Created on 2013-4-19

@author: wwjiang
'''
from django.conf.urls import patterns, include, url


urlpatterns = patterns('reading.views',
        (r'^$', 'default'),
        (r'^all/$', 'reading_all_page')
        (r'^all/page/(?P<page_id>\d+)/$', 'reading_all_page'),
        # 分类读书会列表
        (r'^class/(?P<class_id>\d+)/$', 'reading_class_page'),
        (r'^class/(?P<class_id>\d+)/page/(?P<page_id>\d+)$', 'reading_class_page'),
        # 按举办方分类
        (r'^org/(?P<org_id>\d+)/$', 'reading_org_page'),
        (r'^org/(?P<org_id>\d+)/page/(?P<page_id>\d+)/$', 'reading_org_page'),
        # 读书会搜索
        (r'^search/(?P<key>.+?)/$', 'reading_search'),
        # 单一读书会详细信息
        (r'^detail/(?P<reading_id>\d+)/$', 'reading_detail'),

        
        # 读书会笔记分页
        (r'^(?P<reading_id>\d+)/note/$', 'reading_note_page'),
        (r'^(?P<reading_id>\d+)/note/page/(?P<page_id>\d+)/$', 'reading_note_page'),
        # 读书会笔记提交
        (r'^note/submit/(?P<reading_id>\d+)/$', 'reading_note_submit'),
        # 读书会讲座笔记详细
        (r'^note/detail/(?P<note_id>\d+)/$', 'reading_note_detail'),
        
         # 当日读书会列表
        (r'^date/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'reading_day'),
        (r'^calendar/$', 'getCalendarInfo'),
        (r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/$', 'getCalendarInfo'),
        (r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/{prev|next}/$', 'getCalendarInfo'),    
)
