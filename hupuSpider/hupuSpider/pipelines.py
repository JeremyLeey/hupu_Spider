# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
# 调用os库可以判断文件、文件夹是否存在，并删除之（递归删除文件夹）
import os
import datetime
import requests
import urllib


class HupuspiderPipeline(object):

    id = 1
    placeholder = 'https://b1.hoopchina.com.cn/web/sns/bbs/images/placeholder.png'
    today = datetime.date.today()
    basic_file = 'H://hupubxj_' + '{}-{}-{}'.format(today.year, today.month, today.day)

    title_file = basic_file + '.txt'
    IMAGES_STORE = 'H://pic2'

    if os.path.exists(title_file):
        os.remove(title_file)
    if not os.path.exists(IMAGES_STORE):
        os.mkdir(IMAGES_STORE)

    def process_item(self, item, spider):
        # 伪造header信息
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110'
                          'Safari/536.36',
            'Cookie': 'b963ef2d97e050aaf90fd5fab8e78633'
        }
        with open(self.title_file, 'a+') as f:
                f.write(item['title'] + '\n')
        for jpg_url in item['src']:
            if jpg_url == self.placeholder:
                continue
            filename = 'picture_{}'.format(self.id)
            print(jpg_url)
            with open('{}//{}.jpg'.format(self.IMAGES_STORE, filename), 'wb') as f:
                req = requests.get(jpg_url, headers=header)
                f.write(req.content)
            self.id += 1
        return item
