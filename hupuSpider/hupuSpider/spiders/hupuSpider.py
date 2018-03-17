# -*- coding: utf-8 -*-
import scrapy
import time
import urllib
import re
from hupuSpider.items import HupuspiderItem


def get_pages(basic_url):
    urls = list()
    for i in range(1, 1, 1):
        new_url = basic_url + '-' + str(i)
        urls.append(new_url)
    return urls


class hupuSpider(scrapy.Spider):
    name = 'Hupu_Bxj'

    start_urls = []
    basic_url = 'http://bbs.hupu.com/bxj'
    visited = set()

    # 初始化生成start_urls,这里暂时选取前4页的帖子地址
    for i in range(1, 2, 1):
        start_urls.append(basic_url+'-'+str(i))

    def parse(self, response):
        # 获取每一个li标签下的内容
        topics = response.xpath('//ul[@class="for-list"]/li')
        basic_url = 'https://bbs.hupu.com'
        for topic in topics[1:]:
            # 获取帖子的连接地址
            url = basic_url + topic.xpath(".//div[@class='titlelink box']/a[@class='truetit']/@href").extract_first()
            # 如果某条链接被访问过，就跳过访问
            if url in self.visited:
                continue
            self.visited.add(url)
            # 对于每一个帖子的连接地址，发送一个request请求，将下载完成返回得到的response传递给parse_item回调函数
            request = scrapy.Request(url, callback=self.parse_item)
            # time.sleep(1)
            # 在回调函数内分析返回的网页内容，返回Item对象、dict、Request。返回的Request对象之后会经过scrapy处理，下载相应的内容，并调用设置的callback函数
            yield request

    def parse_item(self, response):
        basic_img_src = 'http://'
        item = HupuspiderItem()
        img_list = response.xpath("//div[@class='quote-content']/p/img/@src").extract()
        img_title = response.xpath("//div[@class='bbs-hd-h1']/h1/text()").extract_first()
        # pattern = re.compile(r'''https://i10.hoopchina.com.cn/.+?jpeg''')

        item['title'] = img_title
        item['src'] = img_list
        yield item





