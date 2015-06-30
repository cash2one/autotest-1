
from django.shortcuts import render_to_response
from main.models import Task
import auth
# from django.template import Template, Context
# from django.template.loader import get_template
# from django import forms
# from django.http import HttpResponse

def task_history(request):
    usr = auth.Auth().getUsr(request)

    taskResult = {
      "0":"PASS",
      "1":"FAIL",
      "2":"DEFAULT"
    }

    if 'platformId' in request.GET:
        platformId = request.GET['platformId']
    else:
        platformId = 1
    taskList = Task.objects.filter(STATUS=3,PLATFORM_ID_id=platformId).order_by("-id");
    if 'platformId' in request.GET:
        return render_to_response('dateapp/task_history_table.html',locals())
    else:
        return render_to_response('dateapp/task_history.html',locals())
