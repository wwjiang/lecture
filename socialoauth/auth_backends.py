'''
Created on 2013-4-27

@author: wwjiang
'''
from django.contrib.auth.models import User

class BackendBase:
    
    def get_cookie_from_request(self,request):
        
        pass
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None
        
class RenrenBackend(BackendBase):
    def authenticate(self,request,user=None):
        cookie = super(RenrenBackend,self).get_cookie_from_request(request)
        if cookie:
            uid = cookie['uid']
            access_token = cookie['access_token']
        else:
            code = request.GET.get('code', '')
            

class SinaBackend(BackendBase):
    def authenticate(self,request):
        pass
    
class QQBackend(BackendBase):
    def authenticate(self,request):
        pass
class DoubanBackend(BackendBase):
    def authenticate(self,request):
        pass

