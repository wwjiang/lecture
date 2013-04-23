'''
Created on 2013-4-20

@author: wwjiang
'''

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^lecture/',include('lecture.urls'))
    (r'^reading/',include('reading.urls'))
    (r'^org/',include('org.urls'))
    (r'^accounts/',include('accounts.urls'))
)

