"""
Base_Url:
Author:
Modify:
"""

import execjs
import requests


class Login(object):

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.sess = requests.session()

    def get_pwd(self):

        js_pwd = """
        
        function getpwd(pwd){
        
        
        
        }
        
        
        """

        pwd = execjs.compile(js_pwd).call("getpwd", self.pwd)
        return pwd

    def login_(self):
        pwd = self.get_pwd()


if __name__ == '__main__':
    user = ""
    pwd = ""

    login = Login(user, pwd)  # TODO: 输入账号&密码
    login.login_()