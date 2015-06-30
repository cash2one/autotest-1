# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from main.models import TESTCASE
from main.models import XMLFILE
from main.models import Platform
from django.utils.encoding import force_unicode, smart_unicode
import StringIO
from django.utils.xmlutils import SimplerXMLGenerator
import json
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
# from django.template import Template, Context
# from django.template.loader import get_template
# from django import forms
from django.http import HttpResponse
import auth
import os
import random
from django import forms
from django.http import HttpResponseRedirect
import time
@csrf_exempt
def datasource_update(request):
    
    try:
        PATH_INFO = request.META['PATH_INFO']
    except KeyError:
        PATH_INFO = 'unknown'
        return HttpResponse("Hello world,Your PATH_INFO is %s" % PATH_INFO)

    platformId = PATH_INFO.split('/')[2]
    datasouceId = PATH_INFO.split('/')[3]
    
    Datasource = XMLFILE.objects.filter(id=datasouceId)[0]
    return render_to_response('dateapp/datasource_update.html',locals())
'''
    try:
            ua = request.META['HTTP_USER_AGENT']
            ub = request.META['REMOTE_ADDR']
            values = request.META.items()
            values.sort()
            html = []
            for k, v in values:
                html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
            return HttpResponse('<table>%s</table>' % '\n'.join(html))
            return render_to_response('dateapp/datasource_update.html',locals())
            
    except KeyError:
            ua = 'unknown'
            ub = 'unknown'
            return HttpResponse("Hello world,Your browser is %s,client is %s" % (ua,ub))
'''

@csrf_exempt
def save_update(request):
    try:
        if  request.is_ajax():
            if request.method == "POST":
                pathName = request.POST.get('pathname',None)
                xmlName = request.POST.get('xmlName',None)
                xmlContent = request.POST.get('xmlContent',None)
                xmlType = int(request.POST.get('xmlType',None))

                platformId = int(pathName.split('/')[2])

                if(pathName.split('/')[3]=="add"):
                    PLATFORM = Platform.objects.filter(id=platformId)       
                    xmlFile = XMLFILE.objects.create(name=xmlName,platformId=PLATFORM[0],content=xmlContent,type=xmlType,status=0)
                    return HttpResponse(json.dumps({"status":"success","platformId":platformId}),mimetype='application/json')

                datasourceId = pathName.split('/')[3]
                XMLFILE.objects.filter(id=datasourceId).update(name=xmlName, content=xmlContent,type=xmlType)
                return HttpResponse(json.dumps({"status":"success","platformId":platformId}),mimetype='application/json')
    except Exception,ex:
        return HttpResponse(json.dumps({"status":ex}),mimetype='application/json')

@csrf_exempt
def delete_yes(request):
    try:
        if request.is_ajax() :
            if request.method == "POST":
                pathName = request.POST.get('pathname',None)

                platformId = int(pathName.split('/')[2])


                if(pathName.split('/')[3]=="add"):
                    return HttpResponse(json.dumps({"status":"success","platformId":platformId}),mimetype='application/json')

                datasourceId = int(pathName.split('/')[3])
                XMLFILE.objects.filter(id=datasourceId).update(status=1)
                return HttpResponse(json.dumps({"status":"success","platformId":platformId}),mimetype='application/json')
    except Exception,ex:
        return HttpResponse(json.dumps({"status":ex}),mimetype='application/json')


@csrf_exempt
def delete_selected(request):
    try:
        if request.is_ajax():
            if request.method =="POST":
                selectedIds = request.POST.get('selectedIds',None)
                selected_Ids =selectedIds.split(',')
                #num = len(selected_Ids)
                #platformId =""
                for id in selected_Ids:
                    if int(id)>0:
                        XMLFILE.objects.filter(id=id).update(status=1)
                        platformId = str(XMLFILE.objects.get(id=id).platformId)
                        #platformId =XMLFILE.objects.filter(id=id).values('platformId')[0]['platformId']
                return HttpResponse(json.dumps({"status":"success","platformId":platformId}),mimetype='application/json')
    except Exception,ex:
        return HttpResponse(json.dumps({"status":ex}),mimetype='application/json')

@csrf_exempt
def export_excel(request):
        try:
            PATH_INFO = request.META['PATH_INFO']

        except KeyError:
            PATH_INFO = 'unknown'
            return HttpResponse("Hello world,Your PATH_INFO is %s" % PATH_INFO)

        selectedIds = PATH_INFO.split('/')[3]
        selected_Ids =selectedIds.split(',')

        #num = len(selected_Ids)
        str_xml=""
        for id in selected_Ids:
            if int(id)>0:
                try:
                    str_xml= str(XMLFILE.objects.get(id=id).content)
                    str_xmlName = str(XMLFILE.objects.get(id=id).name)
                except ObjectDoesNotExist:
                    return HttpResponse(json.dumps({"status":"Either the entry or blog doesn't exist."}),mimetype='application/json')
                response =  HttpResponse(str_xml,mimetype='text/xml')
                #'application/octet-stream')
                response['Content-Type'] = 'application/force-download'
                Content = 'attachment; filename='+str_xmlName+'.xml'
                response['Content-Disposition'] = Content
                return response
                #return HttpResponse(json.dumps({"status":"success","xmlContent":str_xml}),mimetype='application/json')


@csrf_exempt
def upload_file(request):
    # 获取文件
    if request.method == 'POST':
        file_obj = request.FILES.get('your_file', None)
        try:
            PATH_INFO = request.META['PATH_INFO']
        except KeyError:
            PATH_INFO = 'unknown'
            return HttpResponse("Hello world,Your PATH_INFO is %s" % PATH_INFO)

        platformId = PATH_INFO.split('/')[2]
        if file_obj == None:
            return HttpResponse('file not existing in the request')
        #handle_uploaded_file(file_obj)
        HERE = os.path.dirname(os.path.abspath(__file__))
        #file_name = 'temp_file-%d' % random.randint(0,100000) # 不能使用文件名称，因为存在中文，会引起内部错误
        time_now = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        file_name='%s-%s'% (file_obj._name,time_now)
        file_full_path = os.path.join(HERE+'/temp_files/',file_name).replace('/','\\')

        with open(file_full_path,'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        file = open(file_full_path,'r')
        try:
            lines = file.read()
        finally:
            file.close()

        xml_content=lines
        xml_name=str(file_obj._name)
        PLATFORM = Platform.objects.filter(id=platformId)
        xmlFile = XMLFILE.objects.create(name=xml_name,platformId=PLATFORM[0],content=xml_content,type=0,status=0)
        return HttpResponseRedirect('/datasource_info/')


'''
    # 写入文件
    HERE = os.path.dirname(os.path.abspath(__file__))
    #HERE = os.path.join(HERE, '../')
    file_name = 'temp_file-%d' % random.randint(0,100000) # 不能使用文件名称，因为存在中文，会引起内部错误
    file_full_path = os.path.join(HERE+'/temp_files/',file_name).replace('/','\\')
    dest = open(file_full_path,'wb+')
    dest.write(file_obj.read())
    dest.close()
'''
def handle_uploaded_file(f):
    HERE = os.path.dirname(os.path.abspath(__file__))
    file_name = 'temp_file-%d' % random.randint(0,100000) # 不能使用文件名称，因为存在中文，会引起内部错误
    file_full_path = os.path.join(HERE+'/temp_files/',file_name).replace('/','\\')
    lines=""
    with open(file_full_path,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

