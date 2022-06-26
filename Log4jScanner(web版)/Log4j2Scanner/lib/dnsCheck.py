#!/usr/bin/env python
# -*- coding:utf-8 -*-
import copy

import requests

from lib.payload import trans


class Dnslog():
    def __init__(self):
        self.count = 0
        self.url = ''
        self.getdnssub_url = 'http://www.dnslog.cn/getdomain.php'
        self.getres_url = 'http://www.dnslog.cn/getrecords.php'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X '
        }
        self.s = requests.session()  # 这里顶一个session，同一个session可以拿到之前获取到的子域名的日志啦

    def req(self):  # 获取请求到的dnslog随机子域名
        try:
            req = self.s.get(url=self.getdnssub_url, headers=self.headers, allow_redirects=False, verify=False,
                             timeout=30)
            self.url = req.text
            return req.text
        except:
            return None

    def res(self):  # 获取dnslog随机子域名的dns查询日志
        try:
            res = self.s.get(url=self.getres_url, headers=self.headers, allow_redirects=False, verify=False, timeout=30)
            # print "dnslog content: "
            # print res.text
            # print self.url
            if self.url in res.text:
                return True
            else:
                return False
            # return res.text
        except:
            return None

    # urlInstance : urlClass 实例
    # header : http头部字段
    # payload : 本次检测使用的paylaod
    def check(self, urlInstance, header, payload, checkHeaders):
        try:
            dnsurl = self.req()

            # payload 构造
            payloads = trans(payload, dnsurl)

            print payloads
            print "\n\n\n################### new Line #########################\n\n\n"
            for item in payloads:
                # print 'Before Replace: ', item
                # item_url = item.replace("{{dnsIP}}", "["+dnsurl+"]")
                # print "After Replace: ", item_url
                # check = copy.deepcopy(header)
                # for i in checkHeaders:
                #     check[i] = item_url
                # urlInstance.sendPacket(check, item_url)
                # res = self.res()
                detail = urlInstance.sendDetail(self, dnsurl, header, checkHeaders, item)
                print "result: \n", detail
                if detail['status']:
                    # result = {'status': True, 'payload': item}
                    return detail
            return {'status': False}
        except:
            return {'status': False}

    def checkDetail(self, urlInstance, dnsurl, header, payload, checkHeaders):
        try:

            for i in checkHeaders:
                check = copy.deepcopy(header)
                check[i] = payload
                print 'check: ', check
                result = urlInstance.sendDetail(self, dnsurl, check, checkHeaders, payload)
                print "result: \n", result
            return result
        except:
            return {'status': False}
