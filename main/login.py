from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
# from django.template import Template, Context
# from django.template.loader import get_template
# from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import sys
import ldap
import Cookie
import datetime

@csrf_exempt
def login(request):
    if 'userName' not in request.GET:
        return render_to_response('dateapp/login.html',locals())
    if 'passwd' not in request.GET:
        return render_to_response('dateapp/login.html',locals())
    user = request.GET['userName']
    pwd = request.GET['passwd']
    referer = "index"
    if referer in request.META:
        referer = request.META['HTTP_REFERER']
    ldap_host="soda.rd.xxx.com"
    ldap_port="389"
    ldap_path="ldap://" + ldap_host + ":" + ldap_port + "/";
    baseDn="ou=people,dc=rd,dc=xxx,dc=com"
    username="uid=" + user + "," + baseDn
    try:   
            l = ldap.initialize(ldap_path)
            l.protocol_version = ldap.VERSION3
            l.simple_bind_s(username,pwd)
    
            searchScope = ldap.SCOPE_SUBTREE
            searchFiltername = "uid"
            retrieveAttributes = None
            searchFilter = '(' + searchFiltername + "=" + user + ')'
            ldap_result_id = l.search(baseDn, searchScope, searchFilter, retrieveAttributes)
            result_type, result_data = l.result(ldap_result_id, 0)
 
            if(not len(result_data) == 0):
                cookieName = "eadAuto"
                response = HttpResponse();
                response.set_cookie(cookieName,user)#,1800)
                response.write(referer)
                return response 
            else:
                return HttpResponse(0)
    
    except ldap.LDAPError,e:
            print e
            return HttpResponse(0)


def logout(request):
    response = HttpResponse();
    response.delete_cookie("eadAuto")
    return response
