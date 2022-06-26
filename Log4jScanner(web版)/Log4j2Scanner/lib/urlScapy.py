#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Downloader, urlManager
import threading
from urlparse import urlparse, urljoin, parse_qs
from bs4 import BeautifulSoup
from urlClass import urlClass


class SpiderMain(object):
    def __init__(self, root, threadNum):
        self.urls = urlManager.UrlManager(root)
        self.download = Downloader.Downloader()
        self.root = root
        self.threadNum = threadNum

    def _judge(self, domain, url):
        if (url.find(domain) != -1):
            return True
        else:
            return False

    def _parse(self, page_url, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser')
        _news = self._get_new_urls(page_url, soup)
        return _news

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a')
        for link in links:
            new_url = link.get('href')
            new_full_url = urljoin(page_url, new_url)
            if (self._judge(self.root, new_full_url)):
                new_urls.add(new_full_url)
        return new_urls

    def _get_param(self, content):
        soup = BeautifulSoup(content, 'html.parser')

    def craw(self):
        result = []
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _content = []
            th = []
            for i in list(range(self.threadNum)):
                if self.urls.has_new_url() is False:
                    break
                new_url = self.urls.get_new_url()
                print("craw:" + new_url)

                li = urlparse(new_url)

                # 域名
                url = urljoin(new_url, li.path)

                # get参数
                args = [key for key in parse_qs(li.query)]
                # print args

                # TODO
                # post参数

                param = []

                model = urlClass(new_url, url, param, args)
                result.append(model)
                t = threading.Thread(target=self.download.download, args=(new_url, _content))
                t.start()
                th.append(t)
            for t in th:
                t.join()
            for _str in _content:
                if _str is None:
                    continue
                try:
                    new_urls = self._parse(new_url, _str["html"])
                    self.urls.add_new_urls(new_urls)
                except:
                    continue
        return result
