'''
Created on 2013-4-27

@author: wwjiang
'''

renren = {
          'authorize_endpoint':'https://graph.renren.com/oauth/authorize',
          'access_endpoint':'',
          'client_id':'',
          'client_secret':'',
          'redirect_uri':'http://www.whulecture.net/redirect/renren',
          'scope':'',
          }

douban = {
          'authorize_endpoint':'https://www.douban.com/service/auth2/auth',
          'access_endpoint':'https://www.douban.com/service/auth2/token',
          'client_id':'',
          'client_secret':'',
          'redirect_uri':'http://www.whulecture.net/redirect/douban',
          'scope':'',
          }

qq = {
          'authorize_endpoint':'https://graph.qq.com/oauth2.0/authorize',
          'access_endpoint':'https://graph.qq.com/oauth2.0/token',
          'openid_endpoint':'https://graph.qq.com/oauth2.0/me',
          'client_id':'',
          'client_secret':'',
          'redirect_uri':'http://www.whulecture.net/redirect/qq',
          'scope':'',
      }

sina = {
          'authorize_endpoint':'https://api.weibo.com/2/oauth2/authorize',
          'access_endpoint':'https://api.weibo.com/oauth2/access_token',
          'client_id':'',
          'client_secret':'',
          'redirect_uri':'http://www.whulecture.net/redirect/sina',
          'scope':'',
        }

_OAUTH2_MAP = {'sina':sina,'douban':douban,'qq':qq,'renren':renren}

import logging

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse

from Oauth2 import APIClient

def auth_login(request,social):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
        
    auth = _OAUTH2_MAP[social]
    client = APIClient(auth)
    url = client.get_authorize_url()
    return HttpResponseRedirect(url)


def auth_login_done(request,social):
    auth = _OAUTH2_MAP[social]
    user = authenticate(request=request,auth=auth)

    if not user:
        request.COOKIES.pop('session_key', None)
        request.COOKIES.pop('user', None)

        logging.debug("SOCIALAUTH: Couldn't authenticate user with Django, redirecting to Login page")
        return HttpResponseRedirect(reverse('auth_login'))

    login(request, user)
    
    logging.debug("SOCIALAUTH: Successfully logged in with %s!" %social)
    
    next_url = request.GET.get('next')
    if not next_url:
        #得到默认路径
        pass
        
    return HttpResponseRedirect(next_url)
