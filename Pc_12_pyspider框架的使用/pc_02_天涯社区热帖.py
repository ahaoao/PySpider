#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-08-10 11:54:45
# Project: TYSQ

from pyspider.libs.base_handler import *
import pymongo


Client = pymongo.MongoClient(host='localhost', port=27017)
db = Client.TYSQ
collection = db.tianyasq


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://bbs.tianya.cn/hotArticle.jsp', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.td-title > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False, fetch_type='js')
        next = response.doc('.long-pages > a:last-of-type').attr.href  # long-page>a 代表选择父节点为long-pages的所有a结点，a:last-of-type代表
        self.crawl(next, callback=self.index_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        TYSQ = {
            "url": response.url,
            "title": response.doc('title').text(),
            "author": response.doc('.js-vip-check').text().split(' ')[0], # split(' ')[0] 指定获得内容的第一个
            "text": response.doc('.atl-content .bbs-content').text(),
        }
        collection.insert_one(TYSQ)
        return TYSQ