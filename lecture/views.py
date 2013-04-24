'''
Created on 2013-4-18

@author: wwjiang
'''

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from lecture.models import *
from lecture.forms import *
from lecture.context_processors import *

import re


"""
������Ϣ��ҳ
"""
def default(request):
    
    #��ҳ��
    page_id = 1
    per_page = 8
    p = Paginator(LectureModel.objects.all(),per_page)
    lecture_page = p.page(page_id)

    request.num = p.count
    request.page = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('lecture_default.html',
                {
                    'lecture_page':lecture_page,
                },
                context_instance=RequestContext(request,
                    processors=[getCalendarInfo,getClassifyInfo,getCalendarInfo,getHotLectures]
                )
            )
"""
���ս����б�
"""
def lecture_day(request,year,month,day):
    #ת����ʽ��
    lectures = LectureModel.objects.filter(
            date__year=year,
            date__month=month,
            date__day=day
            )
    request.num = lectures.count()
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('lecture_day_list.html',
                {
                    'lectures':lectures,
                    'year':year,
                    'month':month,
                    'day':day,
                },
                context_instance=RequestContext(request,
                    processors=[getCalendarInfo]
                )
            )

"""
ȫ�������б��ҳ
"""
def lecture_all_page(request,page_id=1):
    page_id = int(page_id)
    per_page=8
    p = Paginator(LectureModel.objects.all(),per_page)
    lectures = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('lecture_all_list.html',
                {
                    'lectures':lectures,
                },
                context_instance=RequestContext(request,
                    processors=[getCalendarInfo]
                )
            )


"""
���ི���б��ҳ
"""
def lecture_class_page(request,class_id,page_id=1):
    page_id = int(page_id)
    per_page = 8
    classify = ClassifyModel.objects.get(id=int(class_id))
    p = Paginator(classify.lecturemodel_set.all(),per_page)
    lectures_page = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('lecture_classify_list.html',
                {
                    'lectures_page':lectures_page,
                    'classify_id':class_id,
                },
                context_instance=RequestContext(request,
                    processors=[getCalendarInfo]
                )
            )
    
def lecture_org_page(request,org_id,page_id=1):
    page_id = int(page_id)
    orgModel = OrgModel.objects.get(id=int(org_id))
    p = Paginator(LectureModel.objects.filter(source=orgModel))
    lectures = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    
    return render_to_response('lecture_org.html',
                              {'lectures':lectures},
                              context_instance=RequestContext(request,
                                                              processors=[getCalendarInfo])
                              )

"""
��һ������ϸ��Ϣ��ͼ
"""
def lecture_detail(request,lecture_id):
    lecture = LectureModel.objects.get(id=lecture_id)
    #ʹ�������Լ�
    LectureModel.objects.filter(id=lecture_id).update(
            click_number=lecture.click_number+1)
    #����ʼ�
    notes = LectureNoteModel.objects.filter(lecture=lecture).filter(hasPass=True)
    request.num = LectureNoteModel.objects.filter(lecture=lecture).count()
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
    return render_to_response('lecture_detail.html',
                {
                    'lecture':lecture,
                    'notes':notes,
                },
                context_instance=RequestContext(request,
                    processors=[
                        getCalendarInfo,
                        getClassifyInfo,
                        getHotLectures]
                )
            )


"""
����������ͼ
"""
def lecture_search(request,key):
    #��title,speaker,date,placeѰ��ƥ������
    #��list��ʽ�洢��lectures,�������ظ�
    #Q���ʽ��ʵ��or��ѯ
    lectures = LectureModel.objects.filter(Q(title__icontains=key)|
                                           Q(speaker__icontains=key)|
                                           Q(address__icontains=key))

    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('lecture_search_list.html',
            {'lectures':lectures},
            context_instance=RequestContext(request))

"""
����¼���б�
"""
def lecture_records_page(request,page_id=1):
    page_id = int(page_id) 
    per_page = 8
    p = Paginator(LectureModel.objects.filter(hasRecord=True),per_page)
    lectures = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('lecture_records.html',
                {
                    'lectures':lectures,
                },
                context_instance=RequestContext(request,
                    processors=[getCalendarInfo,getClassifyInfo,getCalendarInfo,getHotLectures]
                )
            )

"""
�����ʼ��ύ
"""
@login_required
def note_submit(request,lecture_id):
    form = LectureNoteForm()
    lecture = LectureModel.objects.get(id=int(lecture_id))
    #��һ�η���
    if not request.method == "POST":
        return render_to_response('lecture_note_submit.html',
                {
                    'lecture':lecture,
                    'form':form,
                },
                context_instance=RequestContext(request,
                    processors=[getClassifyInfo,getCalendarInfo,getHotLectures]
                )
            )
    
    #��֤���Ϸ���
    form = LectureNoteForm(request.POST)
    if not form.is_valid():
        return render_to_response('lecture_note_submit.html',
                {
                    'lecture':lecture,
                    'form':form,
                },
                context_instance=RequestContext(request,
                    processors=[getClassifyInfo,getCalendarInfo,getHotLectures]
                )
            )

    #�������ʼ�
    data = form.cleaned_data
    note = LectureNoteModel(
                    date=date.today(),
                    time=time.strftime('%H:%M:%S',
                        time.localtime(time.time())
                        ),
                    user=request.user.get_profile(),
                    lecture = lecture,
                    title = data['title'],
                    content = data['content'],
                    hasPass = False,
                    showNote = False,
                    score=0,
                    score_times=0,
                    click_number=0)
    note.save()
    return HttpResponseRedirect("/lecture/"+lecture_id+"/")

"""
�����ʼǷ�ҳ
"""
def lecture_note_page(request,lecture_id,page_id=1):
    page_id = int(page_id)
    per_page = 8
    lecture = LectureModel.objects.get(id=int(lecture_id))
    p = Paginator(LectureNoteModel.objects.filter(lecture=lecture).filter(hasPass=True),per_page)
    notes = p.page(page_id)
    request.num = p.count
    request.page_id = page_id
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('lecture_note_list.html',
                {
                    'lecture':lecture,
                    'notes':notes,
                },
                context_instance=RequestContext(request,
                    processors=[getCalendarInfo]
                )
            )

"""
�����ʼ���ϸ
"""
def note_detail(request,note_id):
    note_id = int(note_id)
    #�����ʼ�
    note = LectureNoteModel.objects.get(id=note_id)
    #ʹ�������Լ�
    LectureNoteModel.objects.filter(id=note_id).update(
            click_number=note.click_number+1)
    #Ϊ��ʹ��{{STATIC_URL}}����ʹ��RequestContext������context
    return render_to_response('lecture_note.html',
                {
                    'note':note,
                },
                context_instance=RequestContext(request,
                    processors=[getClassifyInfo,getCalendarInfo,getHotLectures]
                )
            )
