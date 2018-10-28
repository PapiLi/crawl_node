# -*- coding: utf-8 -*-
import scrapy
from client_node.utils.conn_client import  ClientConnection
from client_node.items import ClientNodeItem

client_id = 1233333
address = None
port=None


class CltspiderSpider(scrapy.Spider):
    name = 'cltspider'
    allowed_domains = ['news.sina.com.cn']
    start_urls = []
    xpath_data={}


    def __init__(self):
        self.connect=ClientConnection(client_id, address, port)
        self.connect.connect()

        start_urls=self.connect.request_tasks()
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse)



    def parse(self, response):
        xpath_data=self.connect.request_xpath.copy()
        item = ClientNodeItem()
        title = response.selector.xpath(xpath_data['title']).extract_first()
        time = response.selector.xpath(xpath_data['time']).extract_first()
        keywords = response.selector.xpath(xpath_data['keywords']).extract_first()
        articles = response.selector.xpath(xpath_data['content']).extract()
        type = response.selector.xpath(xpath_data['type']).extract_first()
        content = ''
        for article in articles:
            if article.isspace():
                continue
            content += (article.lstrip()+ "\n")
        item["title"] = title
        item["time"] = time
        item["keywords"] = keywords
        item["content"] = content
        item["type"]= type
        yield item


