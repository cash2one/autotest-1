from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'autotest.views.home', name='home'),
    # url(r'^autotest/', include('autotest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    url(r'^$','main.index.current_task',name='current_task'),
    url(r'^index','main.index.current_task',name='current_task'),
    url(r'^new_task','main.taskNew.new_task',name='new_task'),    
    url(r'^renew_task','main.taskRenew.renew_task',name='renew_task'),
    url(r'^case_info','main.caseInfo.case_info',name='case_info'),
    url(r'^datasource_info/\d+/\d+/update/$','main.datasource_update.datasource_update',name='datasource_update'),
    url(r'^datasource_info/\d/add/$','main.datasource_add.datasource_add',name='datasource_add'),
    url(r'^datasource_info/$','main.datasourceInfo.datasource_info',name='datasource_info'),
    url(r'^datasource_info/\d/$','main.datasourceInfo.datasource_info',name='datasource_info'),
    url(r'^case_edit','main.caseEdit.case_edit',name='case_edit'),
    url(r'^env_check','main.envCheck.env_check',name='env_check'),
    url(r'^task_history','main.taskHistory.task_history',name='task_history'),
    url(r'^task_report','main.taskReport.task_report',name='task_report'),
    url(r'^login','main.login.login',name='login'),
    url(r'^logout','main.login.logout',name='logout'),
    url(r'^start_task','main.taskNew.start_task',name='start_task'),
    url(r'^save_update','main.datasource_update.save_update',name='save_update'),
    url(r'^delete_yes','main.datasource_update.delete_yes',name='delete_yes'),
    url(r'^delete_selected','main.datasource_update.delete_selected',name='delete_selected'),
    url(r'^datasource_info/\d/upload_file/','main.datasource_update.upload_file',name='upload_file'),
    url(r'^export_excel','main.datasource_update.export_excel',name='export_excel'),
    url(r'^datasource_info/download/','main.datasource_update.export_excel',name='export_excel'),#(?P<selectedId>\d+)/$
    url(r'^restart_task','main.taskNew.restart_task',name='restart_task'),
    url(r'^read_log','main.taskNew.read_log',name='read_log'),
    url(r'^ead_online_version','main.onlineversion_info.onlineversion_info',name='onlineversion_info'),
    url(r'^add_product/$','main.onlineversion_info.add_product',name='add_product'),
    url(r'^test/$','main.onlineversion_info.add_product',name='add_product'),#test jenkins
    
    
)
