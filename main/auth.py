#!/usr/bin/python
# Filename: auth.py



class Auth:
    def __init__(self):
        pass

    def getUsr(self,request):
        usr = ""
        if self.isLogin(request):
            usr = request.COOKIES['eadAuto']
        return usr

    def isLogin(self,request):
        if True == request.COOKIES.has_key('eadAuto'):
            return True;
        return False
