
from django.shortcuts import render_to_response
from main.models import TASKRESULT
from main.models import Task
# from django.template import Template, Context
# from django.template.loader import get_template
# from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import auth
def task_report(request):
    task_result = {
        "0":"PASS",
        "1":"FAIL",
        "2":"NEW"
    }   


    if not auth.Auth().isLogin(request):
        return HttpResponseRedirect('/login')
    else:
        usr = auth.Auth().getUsr(request)

    if 'taskId' in request.GET:
        taskId = request.GET['taskId']
        newestTask = Task.objects.get(id="%s" % taskId)
    else:
        newestTask = Task.objects.filter(LDAP=usr).order_by('-id')[0];
        taskId = newestTask.id
    resList = TASKRESULT.objects.filter(task_id="%s" % taskId);
    #for i in resultList:
    #res.append('<tr><td>%s</td></tr>') % (resultList.suiteId)
    return render_to_response('dateapp/task_report.html',locals())    
