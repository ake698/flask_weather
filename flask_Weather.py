from flask import Flask,jsonify,render_template,request
from sqlalchemy import extract,and_
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
    airs = Airquality.query.filter(and_(extract('month',Airquality.date) == month,
					extract('year',Airquality.date) == year)
					).all()
    print(airs)
    return jsonify(
       result = [i.to_json() for i in airs])


@app.route("/login/")
def login():
    return render_template('login.html')


@app.route("/register/",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get('password')
        print(username,password)
        return jsonify({username:password})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
