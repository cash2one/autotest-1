
from django.shortcuts import render_to_response
from main.models import TESTCASE
from main.models import XMLFILE
from django.views.decorators.csrf import csrf_exempt
# from django.template import Template, Context
# from django.template.loader import get_template
# from django import forms
from django.http import HttpResponse
import auth
@csrf_exempt
def datasource_info(request):
    
    if 'platformId' in request.GET:
        platformId = request.GET['platformId']
    else:
        platformId = 1
    datasouceSet = XMLFILE.objects.filter(platformId_id=platformId,status=0).order_by('-id')
    
    if 'platformId' in request.GET:
        return render_to_response('dateapp/datasource_info_table.html',locals())
    else:
        return render_to_response('dateapp/datasource_info.html',locals())
    #return render_to_response('dateapp/datasource_info.html',locals())#,{'taskset':taskset,'tasknum':tasknum}
