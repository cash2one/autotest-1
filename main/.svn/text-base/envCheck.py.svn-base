
from django.shortcuts import render_to_response
from main.models import ENV
# from django.template import Template, Context
# from django.template.loader import get_template
# from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import auth

def env_check(request):
    if not auth.Auth().isLogin(request):
        return HttpResponseRedirect('/login')
    else:
        usr = auth.Auth().getUsr(request)
    if 'platformId' in request.GET:
        platformId = request.GET['platformId']
    else:
        platformId = 1 

    env_status = {
        "0":"Create",
        "1":"RunOn",
        "2":"Run",
        "3":"Fail",
        "4":"StopOn",
        "5":"Stop",
        "6":"Del",
        "7":"DelOn"
    }
    
    if 'modify' in request.GET:
        envId = request.GET['envId']
        op = request.GET['op']
        env = ENV.objects.get(ENV_ID=envId)
        platformId = env.PLATFORM_ID_id
        handleOp(op,env)

    envList = ENV.objects.filter(LDAP=usr,PLATFORM_ID_id=platformId).exclude(STATUS=6).order_by("-ENV_ID") 
    if 'platformId' in request.GET or 'modify' in request.GET:
        return render_to_response('dateapp/env_check_table.html',locals())#,{'taskset':taskset,'tasknum':tasknum}
    else:
        return render_to_response('dateapp/env_check.html',locals())

def handleOp(op,env):
    env.STATUS = op
    env.save()  
