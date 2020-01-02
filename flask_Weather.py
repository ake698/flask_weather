from flask import Flask,jsonify,render_template,request
from sqlalchemy import extract,and_
from config import db,app
from models import *
db.init_app(app)





@app.route('/')
def index():
    return render_template("index.html")

@app.route("/getlast/")
def getLast():
    air = Airquality.query.order_by(Airquality.date.desc()).first().date
    year = air.year
    month = air.month
    # return jsonify({"date":air.date})
    return jsonify({"year":year,"month":month})




@app.route('/getinfo/<year>/<month>/')
def getInfoByYearMonth(year,month):
    airs = Airquality.query.filter(and_(extract('month',Airquality.date) == month,
					extract('year',Airquality.date) == year)).all()
    print(airs)
    return jsonify(
       result = [i.to_json() for i in airs])


@app.route("/admin/users/")
def userManager():
    return render_template("bk/index.html")




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
    app.run(host="0.0.0.0",debug=True)
