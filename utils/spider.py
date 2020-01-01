#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 21:16
# @Author  : QS
# @File    : spider.py

#北京空气质量数据采集

import requests
import config
from bs4 import BeautifulSoup
from time import sleep
import datetime
import pymysql

conn = pymysql.connect(
    host = config.host,
    user = config.username,
    password = config.password,
    db=config.database,
    port = config.port,
    charset = "utf8"
)
cur = conn.cursor()
sql = "insert into airquality(date,qualityLevel,AQI,PM25,PM10,SO2,NO2,CO,O3) VALUES ('%s','%s',%s,%s,%s,%s,%s,'%s',%s)"
baseUrl = "http://www.tianqihoubao.com"


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

def getUrl():
    res = requests.get(url="http://www.tianqihoubao.com/aqi/beijing-201912.html",headers=headers).text
    soup = BeautifulSoup(res,"html.parser")
    result = soup.find("div",class_="box").find("ul")
    urls = []
    for i in result.findAll("li"):
        urls.append(baseUrl+i.a['href'])
    urls.reverse()

    return urls

def getInfo(url):
    response = requests.get(url=url,headers=headers).text
    # print(response)
    soup = BeautifulSoup(response,'html.parser')
    trs = soup.findAll("tr")
    flag = True
    data = []
    for i in trs:
        if flag:
            flag = False
            continue
        tds = i.findAll("td")
        date = tds[0].text.strip()
        level = tds[1].text.strip()
        AQI = tds[2].text.strip()
        PM25 = tds[4].text.strip()
        PM10 = tds[5].text.strip()
        SO2 = tds[6].text.strip()
        NO2 = tds[7].text.strip()
        CO = tds[8].text.strip()
        O3 = tds[9].text.strip()

        # dateTime_p = datetime.datetime.strptime(date,'%Y-%m-%d')

        # print(date)
        if checkData(date):
            print("准备插入%s的数据"%date)
            tempsql = sql%(date,level,AQI,PM10,PM25,SO2,NO2,CO,O3)
            # print(tempsql)
            cur.execute(tempsql)
            conn.commit()
        else:
            print("已存在数据！！")
            continue
        # data.append([date,level,AQI,PM10,PM25,SO2,NO2,CO,O3])
    # print(data)
# getInfo(33)

def checkData(date):
    tempsql = 'select date from airquality where date="%s"'%date
    result = cur.execute(tempsql)
    if result>0:
        return False
    else:
        return True

def main():
    urls = getUrl()
    for url in urls:
        # print(url)
        getInfo(url)
        sleep(2)
    conn.close()

if __name__ == '__main__':
    main()
