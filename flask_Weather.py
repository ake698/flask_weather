from flask import Flask,jsonify
from config import db,app
from models import *
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getinfo/<year>/<month>/')
def getInfoByYearMonth(year,month):
    # dateTime_p = datetime.datetime.strptime(year-month, '%Y-%m')
    # airs = Airquality.objects.filter(date__year=year).filter(date__month=month)
    # json_data = serializers.serialize('json',airs,ensure_ascii=False)
    # return HttpResponse(json_data, content_type="application/json,charset=utf-8")
    airs = Airquality.query.all()
    return jsonify(airs)

if __name__ == '__main__':
    app.run()
