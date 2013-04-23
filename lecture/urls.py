from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('lecture.views',
        #讲座信息首页
        (r'^$','default'),
        #全部讲座列表分页
        (r'^all/$','lecture_all_page')
        (r'^all/page/(?P<page_id>\d+)/$','lecture_all_page'),
        #分类讲座列表
        (r'^class/(?P<class_id>\d+)/$','lecture_class_page'),
        (r'^class/(?P<class_id>\d+)/page/(?P<page_id>\d+)$','lecture_class_page'),
        #按举办方分类
        (r'^org/(?P<org_id>\d+)/$','lecture_org_page'),
        (r'^org/(?P<org_id>\d+)/page/(?P<page_id>\d+)/$','lecture_org_page'),
        #讲座搜索
        (r'^search/(?P<key>.+?)/$','search'),
        #单一讲座详细信息
        (r'^detail/(?P<lecture_id>\d+)/$','lecture_detail'),

        #讲座录音列表
        (r'^record/$','lecture_records_page'),
        #讲座录音分页,一个讲座只有一条录音
        (r'^record/page/(?P<page_id>\d+)/$','lecture_record_page'),
        
        #讲座笔记分页
        (r'^(?P<lecture_id>\d+)/note/$','lecture_note_page'),
        (r'^(?P<lecture_id>\d+)/note/page/(?P<page_id>\d+)/$','lecture_note_page'),
        #讲座笔记提交
        (r'^note/submit/(?P<lecture_id>\d+)/$','note_submit'),
        #讲座笔记详细
        (r'^note/detail/(?P<note_id>\d+)/$','note_detail'),
        
         #当日讲座列表
        (r'^date/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$','lecture_day'),
        (r'^calendar/$','getCalendarInfo')
        (r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/$','getCalendarInfo')
        (r'^calendar/(?P<year>\d{4})/(?P<month>\d{2}/{prev|next}/$','getCalendarInfo')
)
