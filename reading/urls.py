'''
Created on 2013-4-19

@author: wwjiang
'''
from django.conf.urls import patterns, include, url


urlpatterns = patterns('reading.views',
        (r'^$', 'default'),
        (r'^all/$', 'reading_all_page')
        (r'^all/page/(?P<page_id>\d+)/$', 'reading_all_page'),
        # ���������б�
        (r'^class/(?P<class_id>\d+)/$', 'reading_class_page'),
        (r'^class/(?P<class_id>\d+)/page/(?P<page_id>\d+)$', 'reading_class_page'),
        # ���ٰ췽����
        (r'^org/(?P<org_id>\d+)/$', 'reading_org_page'),
        (r'^org/(?P<org_id>\d+)/page/(?P<page_id>\d+)/$', 'reading_org_page'),
        # ���������
        (r'^search/(?P<key>.+?)/$', 'reading_search'),
        # ��һ�������ϸ��Ϣ
        (r'^detail/(?P<reading_id>\d+)/$', 'reading_detail'),

        
        # �����ʼǷ�ҳ
        (r'^(?P<reading_id>\d+)/note/$', 'reading_note_page'),
        (r'^(?P<reading_id>\d+)/note/page/(?P<page_id>\d+)/$', 'reading_note_page'),
        # �����ʼ��ύ
        (r'^note/submit/(?P<reading_id>\d+)/$', 'reading_note_submit'),
        # ����ὲ���ʼ���ϸ
        (r'^note/detail/(?P<note_id>\d+)/$', 'reading_note_detail'),
        
         # ���ն�����б�
        (r'^date/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'reading_day'),
        (r'^calendar/$', 'getCalendarInfo'),
        (r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/$', 'getCalendarInfo'),
        (r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/{prev|next}/$', 'getCalendarInfo'),    
)
