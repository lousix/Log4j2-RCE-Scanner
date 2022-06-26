#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
from urlparse import urlparse, urljoin
from pybloom_live import BloomFilter

class UrlManager(object):
    def __init__(self, root):
        self.new_urls = set()
        self.old_urls = set()
        self.root = urlparse(root).netloc
        self.bf = BloomFilter(capacity=10000)

    def add_new_url(self, url):
        if url is None:
            return
        urljoin(url, urlparse(url).path)

        if urlparse(url).netloc != self.root:
            return

        # if url not in self.new_urls and url not in self.old_urls:
        #     self.new_urls.add(url)

        if url not in self.bf:
            self.new_urls.add(url)
            self.bf.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
