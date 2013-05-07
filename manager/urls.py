'''
Created on 2013-4-27

@author: wwjiang
'''

from django.conf.urls import patterns


urlpatterns = patterns('manager.views',
    (r'^$','default'),#stat
    (r'^stat/(?P<org_id>\d+)/$','stat'),
    (r'^comment/(?P<org_id>\d+)/$','comment'),
    (r'^content/(?P<org_id>\d+)/$','content'),
    (r'^popularize/(?P<org_id>\d+)/$','popularize'),
    (r'^user/(?P<org_id>\d+)/$','user'),
    (r'^tools/(?P<org_id>\d+)/$','tools'),
)
