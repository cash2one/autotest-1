# Create your views here.
# coding=gbk
from main.models import Task
from django.shortcuts import render_to_response
# from django.template import Template, Context
# from django.template.loader import get_template
# from django import forms
# from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage


#def show_table(num,tablelist):
def current_task(request):
    usr = ""
    if True == request.COOKIES.has_key('eadAuto'):
        usr = request.COOKIES['eadAuto']
    taskset =Task.objects.order_by('-TIME').all()
    tasknum = Task.objects.all().__len__()
    return render_to_response('dateapp/index.html',locals())

'''
    tasklist = Task.objects.all()
    paginator =Paginator(tasklist,20)

    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1

    try:
        taskset = paginator.page(page)
    except (EmptyPage,InvalidPage):
        taskset = paginator.page(paginator.num_pages)

    return render_to_response('dateapp/index.html',locals())
'''
'''
    tasknum= Task.objects.all().__len__()
    if(tasknum<=10):
        taskset= Task.objects.order_by('-TIME')[:tasknum]
    else:
        taskset= Task.objects.order_by('-TIME')[:10]
        
                       
    return render_to_response('dateapp/index.html',locals())
'''








