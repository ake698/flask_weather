from flask import Flask,jsonify,render_template,request,redirect,url_for,session
from sqlalchemy import extract,and_
from config import db,app,adminUser,adminPassword
from models import Airquality,UserInfo
from flask_admin import Admin, AdminIndexView
from admin import Airquality_Plus,UserInfo_Plus,Amin_view
admin = Admin(app,name=u'后台管理',template_mode='bootstrap3')

admin.add_view(Airquality_Plus(session=db.session,name=u"空气质量"))
admin.add_view(UserInfo_Plus(session=db.session,name=u"用户管理"))
admin.add_view(Amin_view(name=u'返回站点', endpoint='/admin/verify/',url='/backIndex/'))

db.init_app(app)


def check(func):
    def inner(*args,**kwargs):
        if not session.get('username'):
            return redirect('/login/')
        return func(*args,**kwargs)
    return inner


@app.route('/')
@app.route('/index/',endpoint='index')
@check
def index():
    return render_template("index.html")





@app.route("/getlast/",endpoint='getLast')
@check
def getLast():
    air = Airquality.query.order_by(Airquality.date.desc()).first().date
    year = air.year
    month = air.month
    # return jsonify({"date":air.date})
    return jsonify({"year":year,"month":month})



@app.route('/getinfo/<year>/<month>/',endpoint='getInfoByYearMonth')
@check
def getInfoByYearMonth(year,month):
    airs = Airquality.query.filter(and_(extract('month',Airquality.date) == month,
					extract('year',Airquality.date) == year)).all()
    # print(airs)
    return jsonify(
       result = [i.to_json() for i in airs])






@app.route("/login/",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get("username")
        password = request.form.get('password')
        if username == adminUser and password == adminPassword:
            session["username"] = "admin"
            return jsonify({"code":0})
        user = UserInfo.query.filter(UserInfo.username==username,UserInfo.password==password).first()
        if user:
            session["username"] = username
            return jsonify({"code":0})

        return jsonify({"code":1})


@app.route("/register/",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get('password')
        if username == "admin":
            return jsonify({"code":3})

        users = UserInfo.query.filter(UserInfo.username==username).all()
        if len(users) > 0:
            return jsonify({"code":1})
        user = UserInfo(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"code":0})


@app.route('/logout/')
def logout():
    session.clear()
    return redirect("/login/")

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
