'''
Created on 2013-4-18

@author: wwjiang
'''
from lecture.models import *
from datetime import date, datetime
import calendar,time


"""
context 处理器
"""
def getHotLectures(request):
    hot_lectures = LectureModel.objects.order_by(
            '-showLecture','-click_number','-date',
            '-hasRecord','-score',
            )[0:5]
    return {'hot_lectures':hot_lectures,}
"""
获取日历信息，context处理器
"""
def getCalendarInfo(request):
    year, month, day = time.localtime()[:3]
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    lst = [[]]
    week = 0
    for mday in month_days:
        entries = current = False
        entries = LectureModel.objects.filter(date__year=year, date__month=month, date__day=mday)
        if day == mday:
            current = True
        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1
    return {
                'year':year,
                'month':month,
                'month_days':lst,
            }

"""
获取分类信息,context处理器
"""
def getClassifyInfo(request):
    lectures = LectureModel.objects.all()
    lecture_classify = LectureClassifyModel.objects.all()
    association_classify = AssociationClassifyModel.objects.all()
    apartment_classify = ApartmentClassifyModel.objects.all()
    return {
                'lecture_classify':lecture_classify,
                'association_classify':association_classify,
                'apartment_classify':apartment_classify,
            }

class Page:
    index = 1
    isCurrent = False

"""
获取分页信息，context处理器，为分页添加信息,为什么不在html里面处理该逻辑？只需要有num和page信息就可以了
"""
def getPagingInfo(request):
    lecture_num = request.num
    curPage = request.page #当前页面
    if lecture_num % 8 == 0:
        page_num = lecture_num / 8
    else:
        page_num = lecture_num / 8 + 1
    Pages = []
    begin = (curPage-1) / 10 * 10 + 1 #显示当前分页所在的10个分页
    if begin + 10 < page_num:
        end = begin + 10
    else:
        end = page_num
    for index in range(begin,end):
        tempPage = Page()
        tempPage.index = index
        if index == curPage:
            tempPage.isCurrent = True
        Pages.append(tempPage)
         
    #nav额外所需数据
    hasPrev = True
    hasNext = True
    if curPage == 1:
        hasPrev = False
    if curPage == page_num:
        hasNext = False
    return {
                'page_num':page_num,
                'hasPrev':hasPrev,
                'hasNext':hasNext,
                'Pages':Pages,
                'prev_page':curPage-1,
                'current_page':curPage,
                'next_page':curPage+1,
            }
