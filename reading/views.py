'''
Created on 2013-4-20

@author: wwjiang
'''
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from reading.models import *
from reading.forms import *

import re,time
from datetime import date


"""
讲座信息首页
"""
def default(request):
    #分页栏
    page_id = 1
    per_page = 8
    p = Paginator(ReadingModel.objects.all(),per_page)
    reading_page = p.page(page_id)

    request.num = p.count
    request.page = page_id
    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('reading_default.html',
                {
                    'reading_page':reading_page,
                },
                context_instance=RequestContext(request)
            )
"""
当日讲座列表
"""
def reading_day(request,year,month,day):
    #转换格式？
    readings = ReadingModel.objects.filter(
            date__year=int(year),
            date__month=int(month),
            date__day=int(day)
            )
    request.num = readings.count()
    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('reading_day_list.html',
                {
                    'readings':readings,
                    'year':year,
                    'month':month,
                    'day':day,
                },
                context_instance=RequestContext(request)
            )

"""
全部读书会列表分页
"""
def reading_all_page(request,page_id=1):
    page_id = int(page_id)
    per_page=8
    p = Paginator(ReadingModel.objects.all(),per_page)
    readings = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('reading_all_list.html',
                {
                    'readings':readings,
                },
                context_instance=RequestContext(request)
            )


"""
分类讲座列表分页
"""
def reading_class_page(request,class_id,page_id=1):
    page_id = int(page_id)
    per_page = 8
    classify = ClassifyModel.objects.get(id=int(class_id))
    p = Paginator(classify.readingmodel_set.all(),per_page)
    readings_page = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('reading_classify_list.html',
                {
                    'readings_page':readings_page,
                    'classify_id':class_id,
                },
                context_instance=RequestContext(request)
            )
    
def reading_org_page(request,org_id,page_id=1):
    page_id = int(page_id)
    orgModel = OrgModel.objects.get(id=int(org_id))
    p = Paginator(ReadingModel.objects.filter(source=orgModel))
    readings = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    
    return render_to_response('reading_org.html',
                              {'readings':readings},
                              context_instance=RequestContext(request))

"""
单一讲座详细信息视图
"""
def reading_detail(request,reading_id):
    reading_id = int(reading_id)
    reading = ReadingModel.objects.get(id=reading_id)
    #使访问量自加
    ReadingModel.objects.filter(id=reading_id).update(
            click_number=reading.click_number+1)
    #读书笔记
    notes = ReadingNoteModel.objects.filter(reading=reading).filter(hasPass=True)
    request.num = ReadingNoteModel.objects.filter(reading=reading).count()
    request.page = 1
    #预览讲座笔记内容
    for note in notes:
        m = re.search('<p>(.+)</p>',note.content)
        try:
            note.content = m.group(1)
        except:
            pass
        if len(note.content) >= 50:
            note.content= note.content[:90]+"........"
    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('reading_detail.html',
                {
                    'reading':reading,
                    'notes':notes,
                },
                context_instance=RequestContext(request)
            )


"""
讲座搜索视图
"""
def reading_search(request,key):
    #从title,date,place寻找匹配数据
    #Q表达式来实现or查询
    readings = ReadingModel.objects.filter(Q(title__icontains=key)|
                                           Q(address__icontains=key))

    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('reading_search_list.html',
            {'readings':readings},
            context_instance=RequestContext(request))



"""
讲座笔记提交
"""
@login_required
def reading_note_submit(request,reading_id):
    form = ReadingNoteForm()
    reading = ReadingModel.objects.get(id=int(reading_id))
    #第一次访问
    if not request.method == "POST":
        return render_to_response('reading_note_submit.html',
                {
                    'reading':reading,
                    'form':form,
                },
                context_instance=RequestContext(request)
            )
    
    #验证表单合法性
    form = ReadingNoteForm(request.POST)
    if not form.is_valid():
        return render_to_response('reading_note_submit.html',
                {
                    'reading':reading,
                    'form':form,
                },
                context_instance=RequestContext(request)
            )

    #保存读书笔记
    data = form.cleaned_data
    note = ReadingNoteModel(
                    date=date.today(),
                    time=time.strftime('%H:%M:%S',
                        time.localtime(time.time())
                        ),
                    user=request.user.get_profile(),
                    reading = reading,
                    title = data['title'],
                    content = data['content'],
                    hasPass = False,
                    showNote = False,
                    score=0,
                    score_times=0,
                    click_number=0)
    note.save()
    return HttpResponseRedirect("/reading/"+reading_id+"/")

"""
讲座笔记分页
"""
def reading_note_page(request,reading_id,page_id=1):
    page_id = int(page_id)
    per_page = 8
    reading = ReadingModel.objects.get(id=int(reading_id))
    p = Paginator(ReadingNoteModel.objects.filter(reading=reading).filter(hasPass=True),per_page)
    notes = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('reading_note_list.html',
                {
                    'reading':reading,
                    'notes':notes,
                },
                context_instance=RequestContext(request)
            )

"""
讲座笔记详细
"""
def note_detail(request,note_id):
    note_id = int(note_id)
    #讲座笔记
    note = ReadingNoteModel.objects.get(id=note_id)
    #使访问量自加
    ReadingNoteModel.objects.filter(id=note_id).update(
            click_number=note.click_number+1)
    #为了使用{{STATIC_URL}}必须使用RequestContext而不是context
    return render_to_response('reading_note.html',
                {
                    'note':note,
                },
                context_instance=RequestContext(request)
            )

