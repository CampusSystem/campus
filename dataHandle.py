# coding:utf-8
import json
from decimal import Decimal

import datetime

import dbfunction
import decimal
from collections import OrderedDict


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


cnn = dbfunction.conn


def transactionGetHandle():
    data = json.loads(dbfunction.getDB_Transaction())
    jsondata = []
    for jsdata in data:
        pid = jsdata["p_id"]
        uid = jsdata["user_id"]
        tr_id = jsdata["tr_id"]
        tr_time = jsdata["tr_time"]
        state = jsdata["state"]

        sqlp = "select p_name from product where p_id =" + pid
        cnn.execute(sqlp)
        resultp = cnn.fetchall()
        (rp,)=resultp[0]

        sqlprice = "select p_price from product where p_id =" + pid
        cnn.execute(sqlprice)
        resultprice = cnn.fetchall()
        (rprice,) = resultprice[0]

        sqlu = "select user_name from user where user_id =" + uid  # username
        cnn.execute(sqlu)
        resultu = cnn.fetchall()
        (ru,) = resultu[0]
        sqlsore = "select score from user where user_id =" + uid  # score
        cnn.execute(sqlsore)
        resultscore = cnn.fetchall()
        (s,) = resultscore[0]
        jdata = OrderedDict()
        jdata["p_name"] = rp
        jdata["user_name"] = ru
        jdata["tr_time"] = tr_time
        jdata["state"] = state
        jdata["score"] = int(float(s))
        jdata["p_price"]=int(float(rprice))
        jsondata.append(jdata)
    tr_data = json.dumps(jsondata, ensure_ascii=False)
    return tr_data


def transactionPostHandle(username, productname):
    sqlp = "select p_id from product where p_name ='" + productname + "'"
    cnn.execute(sqlp)
    resultp = cnn.fetchall()
    (pid,) = resultp[0]
    fpid = int(float(pid))  # 商品ID

    sqlprice = "select p_price from product where p_name ='" + productname + "'"
    cnn.execute(sqlprice)
    resultprice = cnn.fetchall()
    (price,) = resultprice[0]
    fprice = int(float(price))  # 商品费用

    sqlu = "select user_id from user where user_name='" + username + "'"
    cnn.execute(sqlu)
    resultu = cnn.fetchall()
    (uid,) = resultu[0]
    fuid = int(float(uid))  # 用户ID

    sqlscore = "select score from user where user_name='" + username + "'"
    cnn.execute(sqlscore)
    resultscore = cnn.fetchall()
    (score,) = resultscore[0]
    score = int(float(score))  # 用户消费后积分
    score -= fprice
    print(score)
    scoreinsert = "update user set score=" + str(score) + " where user_name='" + username + "'"
    cnn.execute(scoreinsert)
    dbfunction.db.commit()  # 提交执行
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    index = 4

    sql = "insert into transaction values(%s,%s,%s,%s,%s)" % \
          (fpid, fuid, index,"'" +now+"'", 1)
    print(sql)
    index += 1
    try:
        # 执行SQL语句
        cnn.execute(sql)
        # 提交到数据库执行
        dbfunction.db.commit()
    except:
        # 发生错误时回滚
        dbfunction.db.rollback()


# def activityHandel():

def adminLogin(name):
    sql_id = "select admin_id from admin where admin_username='" + name + "'"
    cnn.execute(sql_id)
    re = cnn.fetchall()
    (id,) = re[0]
    adminid = int(float(id))
    sql_pass = "select admin_password from admin where admin_username='" + name + "'"
    cnn.execute(sql_pass)
    (repass,) = cnn.fetchall()
    password = repass[0]

    # jsondata = []
    jdata = OrderedDict()
    jdata["admin_id"] = adminid
    jdata["admin_username"] = name
    jdata["admin_password"] = password
    # jsondata.append(jdata)
    tr_data = json.dumps(jdata)

    return tr_data


def loginJudge(name, password):
    sql_pass = "select admin_password from admin where admin_username='" + name + "'"
    cnn.execute(sql_pass)
    repass = cnn.fetchall()
    if repass:
        (password1,) = repass[0]
        # print(password1)
        if password == password1:
            return True
    return False


# 活动通过后积分增加
def scoreApply(itableid):
    sql_user = "select user_id from integral_table where itable_id=" + str(itableid)
    cnn.execute(sql_user)
    resultp = cnn.fetchall()
    (uid,) = resultp[0]
    userid = int(float(uid))  # userID
    sql_activity = "select activity_id from integral_table where itable_id=" + str(itableid)
    cnn.execute(sql_activity)
    resulta = cnn.fetchall()
    (aid,) = resulta[0]
    actid = int(float(aid))  # activityID
    #
    sqlact_score = "select score from activity where activity_id=" + str(actid)
    cnn.execute(sqlact_score)
    result_actscore = cnn.fetchall()
    (act_score,) = result_actscore[0]
    ascore = int(float(act_score))  # 活动积分

    sqlscore = "select score from user where user_id=" + str(userid)
    cnn.execute(sqlscore)
    resultscore = cnn.fetchall()
    (score,) = resultscore[0]
    score = int(float(score))  # 用户积分
    score += ascore
    scoreinsert = "update user set score=" + str(score) + " where user_id=" + str(userid)
    cnn.execute(scoreinsert)


def test():
    transactionPostHandle("Apple", "dress")

# print(transactionHandle())
# test()
