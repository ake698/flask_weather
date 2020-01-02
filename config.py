#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 21:02
# @Author  : QS
# @File    : config.py

import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

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

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config.from_object(Config)
db = SQLAlchemy(app)
