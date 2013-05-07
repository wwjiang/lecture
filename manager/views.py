'''
Created on 2013-4-27

@author: wwjiang
'''
from django.contrib.auth.decorators import login_required

#根据权限决定显示页面
@login_required
def stat(request,org_id):
    #判断权限
    pass

def default(request,org_id):
    return stat(request,org_id)

def comment(request,org_id):
    pass

def content(request,org_id):
    pass
def popularize(request,org_id):
    pass
def user(request,org_id):
    pass
def tools(request,org_id):
    pass
