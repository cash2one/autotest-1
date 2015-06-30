from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Platform(models.Model):
    PLATFORM_NAME = models.CharField(max_length=20)
    PLATFORM_PATH = models.CharField(max_length=60)
    TESTCASE_NAME = models.CharField(max_length=20)
    SOURCEDATA_NAME = models.CharField(max_length=20)
        
    def __unicode__(self):
        return self.PLATFORM_NAME
    class Meta:
        db_table="Platform" 

class ENV(models.Model):
    #SERVICE_IDS = models.CharField(max_length=50)
    ENV_ID = models.AutoField(primary_key=True)
    PLATFORM_ID = models.ForeignKey(Platform)
    LDAP = models.CharField(max_length=30)
    STATUS = models.IntegerField()
    TIME = models.DateTimeField(auto_now_add=True)
    IMPR_SVN = models.CharField(max_length=60)
    RESIN_SVN = models.CharField(max_length=60)
    IMPR_PORT = models.IntegerField()
    RESIN_PORT = models.IntegerField()
    EMMA_PORT = models.IntegerField()
    def __unicode__(self):
        return str(self.ENV_ID)
    class Meta:
        db_table="ENV" 
        
class Task(models.Model): 
    PLATFORM_ID = models.ForeignKey(Platform)
    LDAP = models.CharField(max_length=30)
    TIME = models.DateTimeField(auto_now_add=True)
    STATUS = models.IntegerField()
    RESULT = models.IntegerField()
    LOG_PATH = models.CharField(max_length=1024)
    ENV_ID = models.ForeignKey(ENV)
    USER_CASES = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.LDAP
    class Meta:
        db_table="Task" 
'''    
class Service(models.Model):
    TYPE = models.IntegerField()
    PORT = models.IntegerField()
    STATUS = models.IntegerField()
    ENV_ID = models.ForeignKey(ENV)
    SVN_INFO = models.CharField(max_length=60)
    SVN_VERSION = models.IntegerField()
    
    def __unicode__(self):
        return self.SVN_INFO    
'''

class XMLFILE(models.Model):
    name = models.CharField(max_length=255)
    platformId = models.ForeignKey(Platform)
    content = models.TextField()
    type = models.IntegerField()
    status = models.IntegerField()

    def _unicode_(self):
        return self.name
    class Meta:
        db_table="XmlFile"
        
class TESTCASE(models.Model):
    case_name = models.CharField(max_length=100)
    testsuitID = models.IntegerField()
    Testsuit_name = models.CharField(max_length=100)
    PLATFORM_ID = models.ForeignKey(Platform)
    xml_file = models.ForeignKey(XMLFILE)
    command = models.CharField(max_length=60)
    parameter = models.CharField(max_length=200)
    matchtype = models.CharField(max_length=60)
    Expresult = models.CharField(max_length=1024)
    Detail = models.CharField(max_length=200)
    Log_path = models.CharField(max_length=50)
    status = models.IntegerField()
    
    def __unicode__(self):
        return self.case_name    
    class Meta:
        db_table="TESTCASE"    
        
class TASKRESULT(models.Model):
        task = models.ForeignKey(Task)
        suiteId = models.IntegerField()
        case = models.ForeignKey(TESTCASE)
        result = models.CharField(max_length=255)
        comment = models.TextField()
        
        def __unicode__(self):
                return self.result 
        class Meta:
            db_table="TaskResult" 

