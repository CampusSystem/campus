# coding:utf-8
import json
import MySQLdb
from collections import OrderedDict

import datetime

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="flaskdb", port=3306, charset='utf8')

conn = db.cursor()

# 获得活动
def getDB_Activity():
    sql = "select * from activity"
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for activity in result:
        data = OrderedDict()
        data['activity_id'] = str(activity[0])
        data['activity_name'] = str(activity[1])
        data['activity_des'] = str(activity[2])
        data['activity_begintime'] = str(activity[3])
        data['activity_endtime'] = str(activity[4])
        data['score'] = int(float(activity[5]))
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


def addDB_Activity(name, score, username,des):
    sql = "update activity set activity_des='" + des + "' where activity_name='"+name+"'"
    print(sql)
    sqlscore = "select score from user where user_name='" + username + "'"
    conn.execute(sqlscore)
    resultscore = conn.fetchall()
    (uscore,) = resultscore[0]
    uscore = int(float(uscore))  # 用户消费后积分
    uscore += score
    print(uscore)
    scoreinsert = "update user set score=" + str(uscore) + " where user_name='" + username + "'"
    conn.execute(scoreinsert)
    db.commit()  # 提交执行
    try:
        # 执行SQL语句
        conn.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


def addIntegral(name, des):
    sqlp = "select activity_id from activity where activity_name ='" + des + "'"
    conn.execute(sqlp)
    resultp = conn.fetchall()
    (pid,) = resultp[0]
    fpid = int(float(pid))  # 活动ID
    sqlu = "select user_id from user where user_name ='" + name + "'"
    conn.execute(sqlu)
    resultu = conn.fetchall()
    (uid,) = resultu[0]
    fuid = int(float(uid))  # 用户ID
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")

    sql = "insert into integral_table(user_id,activity_id,itable_id,application_time,finish_case,application_content,application_materials,application_state,note) " \
          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" % \
          (fuid, fpid, 5, "'" + now + "'", "'doing'", "'join'", "'" + name + "'" + "'join'", "'complete'", "'OK'")

    print(sql)
    try:
        # 执行SQL语句
        conn.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


# 获得商品
def getDB_Product():
    sql = "select * from product"
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for product in result:
        data = OrderedDict()
        data['p_id'] = str(product[0])
        data['admin_id'] = str(product[1])
        data['p_name'] = str(product[2])
        data['p_description'] = str(product[3])
        data['p_price'] = int(float(product[4]))
        data['p_place'] = str(product[5])
        data['p_production_date'] = str(product[6])
        data['p_validity'] = str(product[7])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# 交易信息获取  transaction
def getDB_Transaction():
    sql = "select * from transaction "
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for transaction in result:
        data = OrderedDict()
        data['p_id'] = str(transaction[0])
        data['user_id'] = str(transaction[1])
        data['tr_id'] = str(transaction[2])
        data['tr_time'] = str(transaction[3])
        data['state'] = str(transaction[4])

        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# 积分申请表  integral_table
def getDB_ScoreApply():
    sql = "select * from integral_table "
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for transaction in result:
        data = OrderedDict()
        data['user_id'] = str(transaction[0])
        data['activity_id'] = str(transaction[1])
        data['itable_id'] = str(transaction[2])
        data['application_time'] = str(transaction[3])
        data['finish_case'] = str(transaction[4])
        data['application_content'] = str(transaction[5])
        data['application_material'] = str(transaction[6])
        data['application_state'] = str(transaction[7])
        data['note'] = str(transaction[8])

        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


def deleteDB_ScoreApply(id):
    sql = "delete from integral_table where itable_id=" + id
    try:
        # 执行SQL语句
        conn.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


def updateDB_ScoreApply(id, application_time, finish_case, application_content, application_material, application_state,
                        note):
    sql = "update integral_table set " \
          "application_time='" + application_time + "'," + \
          "finish_case='" + finish_case + "'," + \
          "application_content='" + application_content + "'," + \
          "application_materials='" + application_material + "'," + \
          "application_state='" + application_state + "'," + \
          "note='" + note + "'" + "where itable_id=" + id

    print(sql)
    try:
        # 执行SQL语句
        conn.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


def addDB_ScoreApply(user_id, activity_id, itable_id, application_time, finish_case, application_content,
                     application_material, application_state,
                     note):
    sql = "insert into integral_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" % \
          (user_id, activity_id, itable_id, "'" + application_time + "'", "'" + finish_case + "'",
           "'" + application_content + "'", "'" + application_material + "'",
           "'" + application_state + "'", "'" + note + "'")
    try:
        # 执行SQL语句
        conn.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


# user
def getDB_User():
    sql = "select * from user"
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for user in result:
        data = OrderedDict()
        data['user_id'] = str(user[0])
        data['admin_id'] = str(user[1])
        data['user_name'] = str(user[2])
        data['user_password'] = str(user[3])
        data['user_major'] = str(user[4])
        data['user_class'] = str(user[5])
        data['score'] = str(user[6])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# add User
def UserAdd(user_id, admin_id, user_name, user_password, user_major, user_class, user_score):
    sql = "insert into user values(%s,%s,%s,%s,%s,%s,%s)" % \
          (user_id, admin_id, "'" + user_name + "'", "'" + user_password + "'", "'" + user_major + "'",
           "'" + user_class + "'", "'" + user_score + "'")
    try:
        # 执行SQL语句
        conn.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


# admin
def getDB_Admin():
    sql = "select * from admin"
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for admin in result:
        data = OrderedDict()
        data['admin_id'] = str(admin[0])
        data['admin_username'] = str(admin[1])
        data['admin_password'] = str(admin[2])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# business
def getDB_Business():
    sql = "select * from business"
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for bs in result:
        data = OrderedDict()
        data['business_id'] = str(bs[0])
        data['admin_id'] = str(bs[1])
        data['business_name'] = str(bs[2])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# add Business
def addBusiness(business_id, admin_id, business_name):
    sql = "insert into business values(%s,%s,%s)" % \
          (business_id, admin_id, "'" + business_name + "'")
    # print(sql)
    try:
        # 执行SQL语句
        conn.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


# publish
def getDB_Publish():
    sql = "select * from publish"
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for bs in result:
        data = OrderedDict()
        data['admin_id'] = str(bs[0])
        data['activity_id'] = str(bs[1])
        data['publish_time'] = str(bs[2])
        data['statement'] = str(bs[3])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# productowner_table
def getDB_ProductOwner():
    sql = "select * from productowner_table"
    conn.execute(sql)
    result = conn.fetchall()
    # conn.close()
    jsondata = []
    for bs in result:
        data = OrderedDict()
        data['p_id'] = str(bs[0])
        data['bussiness_id'] = str(bs[1])
        data['p_number'] = str(bs[2])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas
# conn.close()
