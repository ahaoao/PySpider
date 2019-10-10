#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-08-09 19:36:40
# Project: qunaer

from pyspider.libs.base_handler import *
import pymongo

# 连接数据库
Client = pymongo.MongoClient(host='localhost', port=27017)
db = Client.QNE
collection = db.qunaer


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://travel.qunar.com/travelbook/list.htm', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('li > .tit > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False,
                       fetch_type='js')  # fetcf_type参数调用phantomjs，模拟JavaScript渲染出图片
        next = response.doc('.next').attr.href
        self.crawl(next, callback=self.index_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        qunaer = {
            "url": response.url,
            "title": response.doc('#booktitle').text(),  # 标题
            "date": response.doc('.when .data').text(),  # 出行日期
            "day": response.doc('.howlong .data').text(),  # 出行天数
            "who": response.doc('.who .data').text(),  # 人物
            "text": response.doc('#b_panel_schedule').text(),  # 攻略正文
            "image": response.doc('.cover_img').attr.src  # 头图信息
        }
        collection.insert_one(qunaer)
        return qunaer