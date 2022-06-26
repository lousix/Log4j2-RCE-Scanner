#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urlparse import urlparse,urljoin

class Downloader(object):
    def get(self, url):
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        _str = r.text
        return _str

    def post(self, url, data):
        r = requests.post(url, data)
        _str = r.text
        return _str

    # post 参数
    '''
    def _get_param(self, content, url):
        soup = BeautifulSoup(content, 'html.parser')
        params = set()
        links = soup.find_all('form')
        for link in links:
            print 1111
            inputs = link.find_all('input')
            for input in inputs:
                param = input.get('name')
                if param is not None:
                    params.append(param)
                    print param
        return params
    '''

    def download(self, url, htmls):
        if url is None:
            return None
        _str = {}
        _str["url"] = url
        try:
            r = requests.get(url, timeout=10)
            if r.status_code != 200:
                return None
            _str["html"] = r.text
            # result.append(self._get_param(r.text, url))
        except Exception as e:
            return None
        htmls.append(_str)