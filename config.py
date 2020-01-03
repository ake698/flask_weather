#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 21:02
# @Author  : QS
# @File    : config.py

import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_babelex import Babel


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

     # database
host = "119.29.79.210"
port = 3306
username = "root"
password = "redhat"
database = "flaskdemo"

class Config(object):
         #格式为mysql+pymysql://数据库用户名:密码@数据库地址:端口号/数据库的名字?数据库格式
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.\
    format(username, password, host, port, database)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False
    FLASK_ADMIN_SWATCH = 'cerulean'
    SECRET_KEY = "fadsfhasdkjfj"
    BABEL_DEFAULT_LOCALE = "zh_CN"

app = Flask(__name__)
# admin = Admin(app,name='flask_Weather',template_mode='bootstrap3')

app.config.from_object(Config)
babel = Babel(app)
db = SQLAlchemy(app)

adminUser = "admin"
adminPassword = "123456"