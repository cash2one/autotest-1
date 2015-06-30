
from django.shortcuts import render_to_response
from main.models import TESTCASE
from main.models import XMLFILE
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# from django.template import Template, Context
# from django.template.loader import get_template
# from django import forms
from django.http import HttpResponse
import auth
@csrf_exempt
def case_info(request):
    usr = auth.Auth().getUsr(request)
    platformId = '1'
    searchText = ''
    searchType = 0
    pageNum = 1

    if 'platformId' in request.GET:
        platformId = request.GET['platformId']
    
    if 'pageNum' in request.GET:
        pageNum = request.GET['pageNum']

    if 'searchText' in request.GET:
        platformId =  request.GET['platformId']
        searchType =  request.GET['searchType']
        searchText =  request.GET['searchText']
        if searchType == '0':
            testCases = TESTCASE.objects.filter(PLATFORM_ID_id=platformId,Testsuit_name__icontains=searchText,status=0).order_by("id")
        elif searchType == '1':
            testCases = TESTCASE.objects.filter(PLATFORM_ID_id=platformId,case_name__icontains=searchText,status=0).order_by("id")
    else:
        testCases = TESTCASE.objects.filter(PLATFORM_ID_id=platformId,status=0).order_by("id")

    numInPage = 15
    paginator = Paginator(testCases, numInPage)
    testCase = paginator.page(pageNum)
    totalPage = len(testCases)/numInPage + 1

    if 'part' in request.GET:
        return render_to_response('dateapp/case_info_table.html',locals())
    else:
        return render_to_response('dateapp/case_info.html',locals())
