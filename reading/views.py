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
������Ϣ��ҳ
"""
def default(request):
    #��ҳ��
    page_id = 1
    per_page = 8
    p = Paginator(ReadingModel.objects.all(),per_page)
    reading_page = p.page(page_id)

    request.num = p.count
    request.page = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('reading_default.html',
                {
                    'reading_page':reading_page,
                },
                context_instance=RequestContext(request)
            )
"""
���ս����б�
"""
def reading_day(request,year,month,day):
    #ת����ʽ��
    readings = ReadingModel.objects.filter(
            date__year=int(year),
            date__month=int(month),
            date__day=int(day)
            )
    request.num = readings.count()
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
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
ȫ��������б��ҳ
"""
def reading_all_page(request,page_id=1):
    page_id = int(page_id)
    per_page=8
    p = Paginator(ReadingModel.objects.all(),per_page)
    readings = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('reading_all_list.html',
                {
                    'readings':readings,
                },
                context_instance=RequestContext(request)
            )


"""
���ི���б��ҳ
"""
def reading_class_page(request,class_id,page_id=1):
    page_id = int(page_id)
    per_page = 8
    classify = ClassifyModel.objects.get(id=int(class_id))
    p = Paginator(classify.readingmodel_set.all(),per_page)
    readings_page = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
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
��һ������ϸ��Ϣ��ͼ
"""
def reading_detail(request,reading_id):
    reading_id = int(reading_id)
    reading = ReadingModel.objects.get(id=reading_id)
    #ʹ�������Լ�
    ReadingModel.objects.filter(id=reading_id).update(
            click_number=reading.click_number+1)
    #����ʼ�
    notes = ReadingNoteModel.objects.filter(reading=reading).filter(hasPass=True)
    request.num = ReadingNoteModel.objects.filter(reading=reading).count()
    request.page = 1
    #Ԥ�������ʼ�����
    for note in notes:
        m = re.search('<p>(.+)</p>',note.content)
        try:
            note.content = m.group(1)
        except:
            pass
        if len(note.content) >= 50:
            note.content= note.content[:90]+"........"
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('reading_detail.html',
                {
                    'reading':reading,
                    'notes':notes,
                },
                context_instance=RequestContext(request)
            )


"""
����������ͼ
"""
def reading_search(request,key):
    #��title,date,placeѰ��ƥ������
    #Q���ʽ��ʵ��or��ѯ
    readings = ReadingModel.objects.filter(Q(title__icontains=key)|
                                           Q(address__icontains=key))

    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('reading_search_list.html',
            {'readings':readings},
            context_instance=RequestContext(request))



"""
�����ʼ��ύ
"""
@login_required
def reading_note_submit(request,reading_id):
    form = ReadingNoteForm()
    reading = ReadingModel.objects.get(id=int(reading_id))
    #��һ�η���
    if not request.method == "POST":
        return render_to_response('reading_note_submit.html',
                {
                    'reading':reading,
                    'form':form,
                },
                context_instance=RequestContext(request)
            )
    
    #��֤���Ϸ���
    form = ReadingNoteForm(request.POST)
    if not form.is_valid():
        return render_to_response('reading_note_submit.html',
                {
                    'reading':reading,
                    'form':form,
                },
                context_instance=RequestContext(request)
            )

    #�������ʼ�
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
�����ʼǷ�ҳ
"""
def reading_note_page(request,reading_id,page_id=1):
    page_id = int(page_id)
    per_page = 8
    reading = ReadingModel.objects.get(id=int(reading_id))
    p = Paginator(ReadingNoteModel.objects.filter(reading=reading).filter(hasPass=True),per_page)
    notes = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('reading_note_list.html',
                {
                    'reading':reading,
                    'notes':notes,
                },
                context_instance=RequestContext(request)
            )

"""
�����ʼ���ϸ
"""
def note_detail(request,note_id):
    note_id = int(note_id)
    #�����ʼ�
    note = ReadingNoteModel.objects.get(id=note_id)
    #ʹ�������Լ�
    ReadingNoteModel.objects.filter(id=note_id).update(
            click_number=note.click_number+1)
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('reading_note.html',
                {
                    'note':note,
                },
                context_instance=RequestContext(request)
            )

