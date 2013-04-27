'''
Created on 2013-4-19

@author: wwjiang
'''
from django.conf.urls import patterns,url


urlpatterns = patterns('reading.views',
        url(r'^$', 'default'),
        url(r'^all/$', 'reading_all_page'),
        url(r'^all/page/(?P<page_id>\d+)/$', 'reading_all_page'),
        # ���������б�
        url(r'^class/(?P<class_id>\d+)/$', 'reading_class_page'),
        url(r'^class/(?P<class_id>\d+)/page/(?P<page_id>\d+)$', 'reading_class_page'),
        # ���ٰ췽����
        url(r'^org/(?P<org_id>\d+)/$', 'reading_org_page'),
        url(r'^org/(?P<org_id>\d+)/page/(?P<page_id>\d+)/$', 'reading_org_page'),
        # ���������
        url(r'^search/(?P<key>.+?)/$', 'reading_search'),
        # ��һ�������ϸ��Ϣ
        url(r'^detail/(?P<reading_id>\d+)/$', 'reading_detail'),

        
        # �����ʼǷ�ҳ
        url(r'^(?P<reading_id>\d+)/note/$', 'reading_note_page'),
        url(r'^(?P<reading_id>\d+)/note/page/(?P<page_id>\d+)/$', 'reading_note_page'),
        # �����ʼ��ύ
        url(r'^note/submit/(?P<reading_id>\d+)/$', 'reading_note_submit'),
        # ����ὲ���ʼ���ϸ
        url(r'^note/detail/(?P<note_id>\d+)/$', 'reading_note_detail'),
        
         # ���ն�����б�
        url(r'^date/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'reading_day'),
        url(r'^calendar/$', 'getCalendarInfo'),
        url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/$', 'getCalendarInfo'),
        url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/{prev|next}/$', 'getCalendarInfo'),    
)
