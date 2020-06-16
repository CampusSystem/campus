# coding:utf-8
from flask import Flask, render_template, request, Response
import dbfunction, dataHandle
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/activity', methods=['GET', 'POST'])
def getActivity():
    if request.method == 'GET':
        db_data = dbfunction.getDB_Activity()
        data = {
            "code": 200,
            "message": 1,
            "data": {
                "total": 30,
                "items": json.loads(db_data)
            }
        }
        return data
    if request.method == 'POST':
        recv_data = request.get_data()
        json_re = json.loads(recv_data)
        dbfunction.addDB_Activity(json_re.get("name"), 1,json_re.get("score"), json_re.get("descript"))  # 获得签到活动信息
        return " "

@app.route('/activitylist', methods=['GET', 'POST'])
def getActivityAndro():
    if request.method == 'GET':
        return dbfunction.getDB_Activity()
    if request.method == 'POST':
        recv_data = request.get_data()
        json_re = json.loads(recv_data)
        dbfunction.addIntegral(json_re.get("name"), json_re.get('descript'))  # 获得签到活动信息
        return " "


@app.route('/transaction', methods=['GET', 'POST'])
def getTransaction():
    if request.method == 'GET':
        return dataHandle.transactionGetHandle()
    if request.method == 'POST':  # 交易完成扣除积分
        recv_data = request.get_data()
        json_re = json.loads(recv_data)
        username = json_re.get("name")
        productname = json_re.get("descript")
        print(username+productname)
        dataHandle.transactionPostHandle(username, productname)
        return " "


@app.route('/order/list', methods=['GET', 'POST'])  # web积分订单
def tran():
    if request.method == 'GET':
        db_data = dbfunction.getDB_Transaction()
        data = {
            "code": 200,
            "message": 1,
            "data": {
                "total": 30,
                "items": json.loads(db_data)
            }
        }

        return data


@app.route('/publish')
def getPublish():
    return dbfunction.getDB_Publish()


@app.route('/product', methods=['GET', 'POST'])
def getProduct():
    if request.method == 'GET':
        db_data = dbfunction.getDB_Product()
        data = {
            "code": 200,
            "message": 1,
            "data": {
                "total": 30,
                "items": json.loads(db_data)
            }
        }

        return data

@app.route('/productlist', methods=['GET', 'POST'])
def getProductAndro():
    if request.method == 'GET':
        return dbfunction.getDB_Product()

@app.route('/business', methods=['GET', 'POST'])
def getBusiness():
    if request.method == 'GET':
        db_data = dbfunction.getDB_Business()
        data = {
            "code": 200,
            "message": 1,
            "data": {
                "total": 30,
                "items": json.loads(db_data)
            }
        }

        return data


@app.route('/business/add', methods=['GET', 'POST'])
def addBusiness():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        business_id = jsondata.get("business_id")
        admin_id = jsondata.get("admin_id")
        business_name = jsondata.get("business_name")
        dbfunction.addBusiness(business_id, admin_id, business_name)

        return " "


@app.route('/user', methods=['GET', 'POST'])
def getUser():
    if request.method == 'GET':
        db_data = dbfunction.getDB_User()
        data = {
            "code": 200,
            "message": 1,
            "data": {
                "total": 30,
                "items": json.loads(db_data)
            }
        }

        return data


# andro
@app.route('/student', methods=['GET', 'POST'])
def getUserAndro():
    if request.method == 'GET':
        db_data = dbfunction.getDB_User()
        return db_data


@app.route('/user/add', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        user_id = jsondata.get("user_id")
        admin_id = jsondata.get("admin_id")
        user_name = jsondata.get("user_name")
        user_password = jsondata.get("user_password")
        user_major = jsondata.get("user_major")
        user_class = jsondata.get("user_class")
        user_score = jsondata.get("user_score")

        dbfunction.UserAdd(user_id, admin_id, user_name, user_password, user_major, user_class, user_score)
        return " "


@app.route('/admin', methods=['GET', 'POST'])
def getAdmin():
    return dbfunction.getDB_Admin()


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        username = jsondata.get("username")
        password = jsondata.get("password")

        rightdata = {
            "code": 200,
            "message": "success",
            "data":
                {
                    "token": dataHandle.adminLogin(username)
                }
        }

        errordata = {
            "code": 404,
            "message": "invalid username or password",
            "data":
                {
                    "token": 1
                }
        }
        if dataHandle.loginJudge(username, password):
            return rightdata
        else:
            return errordata


@app.route('/user/info', methods=['GET', 'POST'])
def userinfor():
    if request.method == 'GET':
        a = request.headers.get("X-Token")
        print("token=" + a)
        data = {
            "code": 200,
            "message": 123,
            "data": json.loads(a)
        }

        return data


# 积分申请表
@app.route('/score/applylist', methods=['GET', 'POST'])
def scoreapplist():
    if request.method == 'GET':
        db_data = dbfunction.getDB_ScoreApply()
        data = {
            "code": 200,
            "message": 1,
            "data": {
                "total": 30,
                "items": json.loads(db_data)
            }
        }

        return data


@app.route('/scoreapply/update', methods=['GET', 'POST'])
def scoreapplist_update():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        id = jsondata.get("itable_id")
        application_time = jsondata.get("application_time")
        finish_case = jsondata.get("finish_case")
        application_content = jsondata.get("application_content")
        application_material = jsondata.get("application_material")
        application_state = jsondata.get("application_state")
        note = jsondata.get("note")

        dbfunction.updateDB_ScoreApply(id, application_time, finish_case, application_content, application_material,
                                       application_state, note)
        if application_state == "examined":
            dataHandle.scoreApply(id)

        data = {
            "code": 200,
            "message": "success update",
            "data": {}
        }

        return data


@app.route('/scoreapply/delete', methods=['GET', 'POST'])
def scoreapplist_delete():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        id = jsondata.get("itable_id")
        dbfunction.deleteDB_ScoreApply(id)

        data = {
            "code": 200,
            "message": "success delete",
            "data": {}
        }

        return data


@app.route('/scoreapply/add', methods=['GET', 'POST'])
def scoreapplist_add():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        user_id = jsondata.get("user_id")
        activity_id = jsondata.get("activity_id")
        itable_id = jsondata.get("itable_id")
        application_time = jsondata.get("application_time")
        finish_case = jsondata.get("finish_case")
        application_content = jsondata.get("application_content")
        application_material = jsondata.get("application_material")
        application_state = jsondata.get("application_state")
        note = jsondata.get("note")

        dbfunction.addDB_ScoreApply(int(str(user_id)), int(str(activity_id)), int(str(itable_id)),
                                    str(application_time), str(finish_case),
                                    str(application_content),
                                    str(application_material),
                                    str(application_state), str(note))

        data = {
            "code": 200,
            "message": "success add",
            "data": {}
        }

        return data


@app.route('/test', methods=['GET', 'POST'])
def getUsers():
    if request.method == 'GET':
        db_data = dbfunction.getDB_ScoreApply()
        data = {
            "code": db_data
        }
        return data


@app.route('/image', methods=['GET', 'POST'])
def getImage():
    if request.method == 'GET':
        with open("image/image001.png", 'rb') as f:
            image = f.read()
        return Response(image, mimetype="image/jpeg")


if __name__ == '__main__':
    print('WebServer Start>>>>>>>>>')
    # app.run()
    app.run(host='0.0.0.0', port=5566)
