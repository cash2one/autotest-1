# coding=UTF-8
from django.contrib import admin
from main.models import Platform,ENV,Task,TESTCASE,XMLFILE


#admin.site.register(Publisher)
#admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book,BookAdmin)
class PlatformAdmin(admin.ModelAdmin):
	list_display = ('id', 'PLATFORM_NAME', 'PLATFORM_PATH','TESTCASE_NAME','SOURCEDATA_NAME') 
	search_fields = ('id','PLATFORM_NAME')

class TaskAdmin(admin.ModelAdmin):
	list_display = ('id','PLATFORM_ID', 'LDAP','STATUS','RESULT','LOG_PATH','USER_CASES','ENV_ID') 
	search_fields = ('id','LDAP')
	
class ENVAdmin(admin.ModelAdmin):
	list_display = ('ENV_ID', 'PLATFORM_ID','LDAP','STATUS','TIME') 
	search_fields = ('ENV_ID','PLATFORM_ID')
'''
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'TYPE', 'PORT','STATUS','ENV_ID','SVN_INFO','SVN_VERSION') 
	search_fields = ('id','SVN_INFO')
'''
class TESTCASEAdmin(admin.ModelAdmin):
	list_display = ('id', 'case_name', 'testsuitID','Testsuit_name','PLATFORM_ID','command','parameter','matchtype','Expresult','Detail','Log_path') 
	search_fields = ('id','case_name')
	
class XMLFILEAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'platformId','content','type') 
	search_fields = ('id','name')
	
admin.site.register(Task,TaskAdmin)
admin.site.register(ENV,ENVAdmin)
#admin.site.register(Service,ServiceAdmin)	
admin.site.register(Platform,PlatformAdmin)
admin.site.register(TESTCASE,TESTCASEAdmin)
admin.site.register(XMLFILE,XMLFILEAdmin)

