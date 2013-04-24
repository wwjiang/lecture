'''
Created on 2013-4-20

@author: wwjiang
'''
from django.conf.urls import patterns


urlpatterns = patterns('org.views',
    (r'^$','default'),
    (r'^detail/(?P<org_id>\d+)/$','org_detail'),
    (r'^message/(?P<org_id>\d+)/$','org_message'),
    (r'^album/(?P<org_id>\d+)/$','org_album'),
    (r'^recruit/(?P<org_id>\d+)/$','org_recruit'),
)

