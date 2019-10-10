#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-08-10 17:12:41
# Project: Ebook

from pyspider.libs.base_handler import *
import pymongo

# 连接数据库
Client = pymongo.MongoClient(host='localhost', port=27017)
db = Client.EBOOK
collection = db.ebook


class Handler(BaseHandler):
    # crawl_config属性，可以将项目的所有爬取配置统一定义到这里，如定义Headers，设置代理等，配置之后全局生效
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.book118.com/nongyegongye/html/nongyegongye_list32-1.html', callback=self.index_page,
                   validate_cert=False)

    # age是任务的有效时间。默认有效时间是10天。
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.mainListName a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)
        next = response.doc('dfn > a').attr.href
        self.crawl(next, callback=self.index_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        ebook = {
            "url": response.url,
            "bookname": response.doc('title').text(),
        }
        collection.insert_one(ebook)
        return ebook