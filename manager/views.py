'''
Created on 2013-4-27

@author: wwjiang
'''
from django.contrib.auth.decorators import login_required

#����Ȩ�޾�����ʾҳ��
@login_required
def stat(request,org_id):
    #�ж�Ȩ��
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
