#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import subprocess

# YAML 文件编写
# protocol : ldap rmi dns iiop ldaps nis corba http nds
# ip => [ip]

# dirtyData:
## ${lower:j}
## ${env:ENV_NAME:-j}
## ${::-j}
## ${date:}
## ${sys:sun.cpu.isalist}


# 运行 zendata生成数据 保存为txt

f = open("fuzzing.txt",'r')
for payload in f.readlines():
    print payload.strip("\n")
    print '111'
