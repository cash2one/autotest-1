# coding=UTF-8
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import sys
pymongoPath = '/global/share/wuhao/pymongo/pymongo-2.6.3-py2.7-linux-x86_64.egg'
sys.path.append(pymongoPath)
import pymongo

import os.path
import sys
import re


reload(sys)
sys.setdefaultencoding('utf8')

productList = ['dict.txt','union.txt','biz.txt','dsp.txt']
productNameList = ['词典产品', '联盟产品', '商业系统产品', 'dsp产品']
@csrf_exempt
def onlineversion_info(request):
    try:
        PATH_INFO = request.META['PATH_INFO']
    except KeyError:
        PATH_INFO = 'unknown'
        return HttpResponse("Hello world,Your PATH_INFO is %s" % PATH_INFO)

    #productGroup = PATH_INFO.split('/')[1]
    path_len = len(PATH_INFO.split('/'))

    HERE = os.path.dirname(os.path.abspath('__file__'))

    if 'product' in request.GET and request.GET['product']:
        product = str(request.GET['product'])
        platform = int(request.GET['platform'])
        action = str(request.GET['action'])
        ##无论在/online_version页面还是/online_version/platform/product页面platform值以请求中的platform参数为准
        '''
        if (path_len==2):
            platform = int(request.GET['platform'])
        elif(path_len==4):
            platform = int(PATH_INFO.split('/')[2])
        else:
            return HttpResponse("something wrong with path_len,PATH_INFO is: %s" % PATH_INFO)
        '''
        fileName = productList[platform-1]
        productFile_path = os.path.join(HERE,'productfile',fileName)

        if action =="add":
            productFile =open(productFile_path,'a')
            productFile.write(('/' + product).decode('utf-8'))
            productFile.close()
        elif action == "delete":
            productFile =open(productFile_path,'r')
            products = productFile.read()
            productFile.close()
            productFile =open(productFile_path,'w')
            products = re.sub('/'+product,'',products)
            productFile.write(products)
            productFile.close()

    productsArray=[]
    for idx,product in enumerate(productList) :
        productFile_path = os.path.join(HERE,'productfile',product)
        productFile = open(productFile_path,'r')
        ##txt文件采用UTF-8无BOM格式编码后 不需要在文件前加/
        #products = productfile.read().split('/')[1:]
        products ={}
        products[0] = productFile.read().split('/')
        products[1] = productNameList[idx]
        productsArray.append(products)
        productFile.close()

    product =""
    if(path_len==2):
        temp_len =len(productsArray[0][0])
        if temp_len != 1:
            product = productsArray[0][0][1]
    elif(path_len==3):
        product = PATH_INFO.split('/')[2]
    else:
        return HttpResponse("something wrong with path_len,PATH_INFO is: %s" % PATH_INFO)

    client = pymongo.MongoClient('nb396x.corp.youdao.com',27017)
    db = client.ticket
    collection = db.Tickets
    ##测试代码
    q1 =re.compile(r'词典')
    q2 = re.compile(r'https://dev.corp.youdao.com/svn/outfox/products/ad/ead/milestones')
    version_arr = collection.find({"productGroup" :1,"product" :product})
    #version_arr = collection.find({"product" :{'$regex':q1},"svnPath":{'$regex':q2}})

    #version_arr = collection.find({'$or':[{"productGroup" :1},{"product" :"伏羲系统"}]})

    return render_to_response('dateapp/onlineversion_info.html',locals())


def add_product(request):
        PATH_INFO = request.META['PATH_INFO']
        productGroup = PATH_INFO.split('/')[1]
        HERE = os.path.dirname(os.path.abspath('__file__'))
        productfile_path = os.path.join(HERE,'productfile',productDict[productGroup])

        if 'product' in request.GET and request.GET['product']:
            product = request.GET['product']
            productfile =open(productfile_path,'a')
            productfile.write('/'+product)

            return render_to_response('dateapp/onlineversion_info.html',locals())

