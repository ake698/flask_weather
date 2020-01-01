#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 20:45
# @Author  : QS
# @File    : db.py

from config import db


class Airquality(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    date = db.Column(db.DATE,unique=True)
    qualityLevel = db.Column(db.String(16))
    AQI = db.Column(db.Integer)
    PM25 = db.Column(db.Integer)
    PM10 = db.Column(db.Integer)
    SO2 = db.Column(db.Integer)
    NO2 = db.Column(db.Integer)
    CO = db.Column(db.String(16))
    O3 = db.Column(db.Integer)

    __tablename__ = "airquality"


if __name__ == '__main__':
    db.create_all()
    print("数据库表格创建完成")