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

    def to_json(self):
        date = "%s年%s月%s日"%(self.date.year,self.date.month,self.date.day)
        return {
		'date':date,'qualityLevel':self.qualityLevel,'AQI':self.AQI,'PM25':self.PM25,'PM10':self.PM10,
		'SO2':self.SO2,'NO2':self.NO2,'CO':self.CO,'O3':self.O3
	}

    def __repr__(self):
        return "%s"%self.date


class UserInfo(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(16))

    def __repr__(self):
        return self.username


if __name__ == '__main__':
    db.create_all()
    print("数据库表格创建完成")
