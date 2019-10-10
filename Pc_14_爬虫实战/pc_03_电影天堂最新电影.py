#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-08-13 16:34:04
# Project: DYTT

from pyspider.libs.base_handler import *
import re
import pymongo
from collections import Iterable


Client = pymongo.MongoClient(host='localhost', port=27017)
db = Client.NewMovie
collection = db.new


class Handler(BaseHandler):
    crawl_config = {
        'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36',
        'Upgrade-Insecure-Requests': '1'}
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.ygdy8.net/html/gndy/china/index.html', callback=self.index_page, validate_cert=False, fetch_type='js')

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('b > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False, fetch_type='js')
        next = response.doc('.x > a:nth-last-child(3)').attr.href
        self.crawl(next, callback=self.index_page, validate_cert=False, fetch_type='js')

    @config(priority=2)
    def detail_page(self, response):
        # 获取下载地址
        Url = response.etree.xpath('//span//tbody//td//a/text()')
        # 获取电影名
        Name = response.doc('h1 > font').text()
        Movie = {
            'MovieName': Name,
            'MovieUrl': Url[0]
        }
        collection.insert_one(Movie)
        return Movie