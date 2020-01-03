#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 20:24
# @Author  : QS
# @File    : admin.py
from flask import request,redirect,url_for,session
# from flask.ext.admin import BaseView, expose
from flask_admin import BaseView,expose
from flask_admin.contrib.sqla import ModelView
from models import Airquality,UserInfo


class Airquality_Plus(ModelView):

    def is_accessible(self):
        if session['username'] == "admin":
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

    def __init__(self,session,**kwargs):
        super(Airquality_Plus,self).__init__(Airquality,session,**kwargs)

class UserInfo_Plus(ModelView):

    def is_accessible(self):
        if session['username'] == "admin":
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

    def __init__(self,session,**kwargs):
        super(UserInfo_Plus,self).__init__(UserInfo,session,**kwargs)


class Amin_view(BaseView):
    @expose("/")
    def index(self):
        return redirect("/index/")

