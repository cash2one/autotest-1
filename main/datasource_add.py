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
def datasource_add(request):
    
    try:
        PATH_INFO = request.META['PATH_INFO']
    except KeyError:
        PATH_INFO = 'unknown'
        return HttpResponse("Hello world,Your PATH_INFO is %s" % PATH_INFO)

    platformId = PATH_INFO.split('/')[2]
    
    #Datasource = XMLFILE.objects.filter(id=datasouceId)[0];
    return render_to_response('dateapp/datasource_add.html',locals())