

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from datetime import date
import time

from models import OrgModel
from models import MessageModel
from forms import MessageForm

def default(request,page_id=1):
    page_id = int(page_id)
    per_page = 8
    p = Paginator(OrgModel.objects.all(),per_page)
    org_page = p.page(page_id)

    request.num = p.count
    request.page = page_id
    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('org_default.html',
                {
                    'org_page':org_page,
                },
                context_instance=RequestContext(request)
            )

def org_detail(request,org_id):
    org_id = int(org_id)
    org = OrgModel.objects.get(id=org_id)
    return render_to_response('org_detail.html',
                {
                    'org':org
                },
                context_instance=RequestContext(request)
            )
    

def org_album(request,org_id):
    pass

def org_recruit(request,org_id):
    pass

@login_required
def org_message(request,org_id):
    org_id = int(org_id)
    form = MessageForm()
    org = OrgModel.objects.get(id=org_id)
    #第一次访问,此时无表单
    if not request.method == "POST":
        return render_to_response('org_message_submit.html',
                {
                    'org':org,
                    'form':form,
                },
                context_instance=RequestContext(request)
            )
    
    #验证表单合法性
    form = MessageForm(request.POST)
    if not form.is_valid():
        return render_to_response('org_note_submit.html',
                {
                    'org':org,
                    'form':form,
                },
                context_instance=RequestContext(request)
            )

    #保存读书笔记
    data = form.cleaned_data
    message = MessageModel(
                    date=date.today(),
                    time=time.strftime('%H:%M:%S',
                        time.localtime(time.time())
                        ),
                    user=request.user.get_profile(),
                    org = org,
                    title = data['title'],
                    content = data['content'],
                    hasPass = False,
                    showNote = False,
                    score=0,
                    score_times=0,
                    click_number=0)
    message.save()
    return HttpResponseRedirect("/org/"+org_id+"/")