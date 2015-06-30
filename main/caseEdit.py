from django.shortcuts import render_to_response
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from main.models import TESTCASE
from main.models import XMLFILE
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
import auth
import string
import os
import logging
import gl
import time
import commands
@csrf_exempt


def case_edit(request):
    gl.logger.info("***************in case edit *******************")
    if not auth.Auth().isLogin(request):
        return HttpResponseRedirect('/login')
    else:
        usr = auth.Auth().getUsr(request)
 
    matchTypeList = ["exact","no"];
    logTypeList = ["logs/log","logs/bid-dsp.log","logs/pv-dsp.log","logs/impr-dsp.log","logs/stat.log","CLICK_TANX","logs/user-context.log","logs/new-user-context.log","CLICK_ADX","CLICK_BEX","CLICK_TADE","CLICK_ALLYES","IMPR_TANX","IMPR_ALLYES","IMPR_TANX_log","IMPR_ADX_log","IMPR_ADX","logs/brand/brandstat.log"];
    
    if 'id' in request.GET:
        caseId = request.GET['id']
        case = TESTCASE.objects.get(id=caseId)
        platformId = case.PLATFORM_ID_id;
        xmlFile = XMLFILE.objects.filter(platformId_id=platformId);
        return render_to_response('dateapp/case_edit.html',locals())
     
    if 'save' in request.GET:
        cases = request.GET['cases']
        platformId = request.GET['platformId']  
        try:
            saveCases(cases,platformId)
        except NotImplementedError:
            return HttpResponse(0)
        return HttpResponse(1)

    if 'deleted' in request.GET:
        cases = request.GET['cases']
        deleteId = json.loads(cases)
        doDelete(deleteId)
        return HttpResponse(1)
    
    if 'add' in request.GET:
        platformId = request.GET['platformId'];
        xmlFile = XMLFILE.objects.filter(platformId_id=platformId);
        return render_to_response('dateapp/case_edit.html',locals())

    if 'copy' in request.GET:
        platformId = request.GET['platformId']
        cases = request.GET['cases']
        copyId = json.loads(cases)
        id = doCopy(copyId)
        return HttpResponse(id)
    
    if 'file' in request.GET:
        file = request.GET['file']
        platformId = request.GET['platformId']
        try:
            dealWithFile(file,platformId,usr)
        except NotImplementedError:
            return HttpResponse(1)
        return HttpResponse(0)

    if 'importXml' in request.GET:
        platformId =  request.GET['platformId']
        filePath = request.GET['filePath']
        importXmlFile(platformId,filePath,usr)
        return HttpResponse(0)
   
    if 'suiteName' in request.GET:
        platformId =  request.GET['platformId']
        suiteName = request.GET['suiteName']
        alltestCase = TESTCASE.objects.filter(PLATFORM_ID_id=platformId,Testsuit_name__icontains=suiteName).order_by("-id");
    elif 'caseName' in request.GET:
        platformId =  request.GET['platformId']
        caseName = request.GET['caseName']
        alltestCase = TESTCASE.objects.filter(PLATFORM_ID_id=platformId,case_name__icontains=caseName).order_by("-id");
        
    else:
        alltestCase = TESTCASE.objects.filter(PLATFORM_ID_id=platformId).order_by("-id");
    numInPage = 15;
    paginator = Paginator(alltestCase, numInPage);
    testCase = paginator.page(pageNum)
    xmlFile = XMLFILE.objects.filter(platformId_id=platformId);
    matchTypeList = ["exact","no"];
    caseNum = len(alltestCase);
    totalPage = len(alltestCase)/numInPage + 1; 
    
    if 'platformId' in request.GET:
        return render_to_response('dateapp/case_edit_table.html',locals())
    else:
        return render_to_response('dateapp/case_edit.html',locals())

def importXmlFile(platformId,filePath,usr):
    targetPath = "/disk1/ead_test/xmlFile/"
    if(os.path.exists(targetPath) == False):
        os.mkdir(targetPath)
    fileList = filePath.split(";")
    for file in fileList:
        targetFile = targetPath + usr + ".tmp"
        file = file.rstrip()
        (status, output) = commands.getstatusoutput("scp %s %s" %(file,targetFile))
        if status==0 :
            caseFile = open(targetFile)
            content = caseFile.read()
            name = os.path.basename(file)
            type = 1
            if "Template" in name:
                type = 0
            if name != "":
                XMLFILE.objects.create(name=name,platformId_id=platformId,content=content,type=type,status=0)
        else:
            gl.logger.error("File %s import error!!" % file)

def insertXmlFile(name,platformId,content,type):
        XMLFILE.objects.create(name=name,platformId_id=platformId,content=content,type=type)


def getXml(name):
    try:
        xmlFiles = XMLFILE.objects.filter(name=name)
        for xmlFile in xmlFiles:
            return xmlFile
    except XMLFILE.DoesNotExist:
        raise NotImplementedError
    raise NotImplementedError

def dealWithFile(file,platformId,usr):
    targetPath = "/disk1/ead_test/caseFile/";
    if(os.path.exists(targetPath) == False):
        os.mkdir(targetPath)
    targetFile = targetPath + usr + ".tmp"
    os.popen("scp " + file + " " + targetFile)
    caseFile = open(targetFile)
    caseList = [];
    for line in caseFile:
        if line.startswith("(ID="):
            name = line.split("):(")[0].split(",")[0].split("=")[1]
            command = line.split("):(")[0].split(",")[1].split("=")[1]
            xml = os.path.basename(line.split("):(")[1])
            param = line.split("):(")[2]
            log = line.split("):(")[3]
            matchType = line.split("):(")[4]
            if len(line.split("):("))==8:
               expect = line.split("):(")[5]
               suiteId = line.split("):(")[6]
               suiteName = line.split("):(")[7][0:-2]
            else:
               expect = line.split("):(")[5][0:-2]
               suiteId = 0
               suiteName = "suite0"
            try:
               gl.logger.info("xmlFilenaume=======================" + xml);
               xmlFile = getXml(xml)
               tc = TESTCASE(case_name=name,testsuitID=suiteId,Testsuit_name=suiteName,PLATFORM_ID_id=platformId,xml_file=xmlFile,command=command,parameter=param,matchtype=matchType,Expresult=expect,Log_path=log,status=0)
               caseList.append(tc)
            except NotImplementedError:
               gl.logger.info(xml + "file does not exist!")
               raise NotImplementedError
    
    for case in caseList:
        case.save()

def saveCases(cases,platformId):
    case = json.loads(cases)
    id = case['id']
    name = case['name']
    suiteId = case['suiteId']
    suiteName = case['suiteName']
    xml = case['xml']
    command = case['command']
    param = case['param']
    matchType = case['matchType']
    expect = case['expect']
    log = case['log']
    detail = case['detail']
    if id!="":
        doUpdate(id,platformId,name,suiteId,suiteName,xml,command,param,matchType,expect,log,detail)
    else:
        doSave(name,suiteId,suiteName,platformId,xml,command,param,matchType,expect,log,detail)

def doDelete(delete):
    for id in delete:
        TESTCASE.objects.filter(id=id).update(status=1)

def doCopy(copy):
    for id in copy:
        testCase = TESTCASE.objects.get(id=id)
        c1 = TESTCASE.objects.create(case_name=testCase.case_name,testsuitID=testCase.testsuitID,Testsuit_name=testCase.Testsuit_name,PLATFORM_ID_id=testCase.PLATFORM_ID_id,xml_file=testCase.xml_file,command=testCase.command,parameter=testCase.parameter,matchtype=testCase.matchtype,Expresult=testCase.Expresult,Log_path=testCase.Log_path,status=0)
        return c1.id

def doUpdate(id,platformId,name,suiteId,suiteName,xml,command,param,matchType,expect,log,detail):
    try:
        xmlFile = getXml(xml);
    except XMLFILE.DoesNotExist:
        raise NotImplementedError;   
    if not xmlFile:
        raise NotImplementedError;   
    TESTCASE.objects.filter(id=id).update(case_name=name,testsuitID=suiteId,Testsuit_name=suiteName,PLATFORM_ID=platformId,xml_file=xmlFile,command=command,parameter=param,matchtype=matchType,Expresult=expect,Log_path=log,Detail=detail)
    return platformId;

def doSave(name,suiteId,suiteName,platformId,xml,command,param,matchType,expect,log,detail):
    try:
        xmlFile = getXml(xml);
    except XMLFILE.DoesNotExist:
        raise NotImplementedError;   
    if xmlFile: 
        TESTCASE.objects.create(case_name=name,testsuitID=suiteId,Testsuit_name=suiteName,PLATFORM_ID_id=platformId,xml_file=xmlFile,command=command,parameter=param,matchtype=matchType,Expresult=expect,Log_path=log,status=0,Detail=detail)
    else:
        raise NotImplementedError;
