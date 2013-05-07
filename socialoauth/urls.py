'''
Created on 2013-4-27

@author: wwjiang
'''

from django.conf.urls import patterns,url

urlpatterns = patterns('socialoauth.views',
      url(r'^signup/auth/(?P<social>\w+)/$','auth_authorize'),
      url(r'^redirect/(?P<social>\w+)/$','auth_redirect'),                     
)
