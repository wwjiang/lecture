from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('lecture.views',
        #������Ϣ��ҳ
        (r'^$','default'),
        #ȫ�������б��ҳ
        (r'^all/$','lecture_all_page')
        (r'^all/page/(?P<page_id>\d+)/$','lecture_all_page'),
        #���ི���б�
        (r'^class/(?P<class_id>\d+)/$','lecture_class_page'),
        (r'^class/(?P<class_id>\d+)/page/(?P<page_id>\d+)$','lecture_class_page'),
        #���ٰ췽����
        (r'^org/(?P<org_id>\d+)/$','lecture_org_page'),
        (r'^org/(?P<org_id>\d+)/page/(?P<page_id>\d+)/$','lecture_org_page'),
        #��������
        (r'^search/(?P<key>.+?)/$','search'),
        #��һ������ϸ��Ϣ
        (r'^detail/(?P<lecture_id>\d+)/$','lecture_detail'),

        #����¼���б�
        (r'^record/$','lecture_records_page'),
        #����¼����ҳ,һ������ֻ��һ��¼��
        (r'^record/page/(?P<page_id>\d+)/$','lecture_record_page'),
        
        #�����ʼǷ�ҳ
        (r'^(?P<lecture_id>\d+)/note/$','lecture_note_page'),
        (r'^(?P<lecture_id>\d+)/note/page/(?P<page_id>\d+)/$','lecture_note_page'),
        #�����ʼ��ύ
        (r'^note/submit/(?P<lecture_id>\d+)/$','note_submit'),
        #�����ʼ���ϸ
        (r'^note/detail/(?P<note_id>\d+)/$','note_detail'),
        
         #���ս����б�
        (r'^date/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$','lecture_day'),
        (r'^calendar/$','getCalendarInfo')
        (r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/$','getCalendarInfo')
        (r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/{prev|next}/$','getCalendarInfo')
)
