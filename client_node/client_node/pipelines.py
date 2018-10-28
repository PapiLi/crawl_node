# -*- coding: utf-8 -*-
from client_node.utils.conn_client import  ClientConnection

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ClientNodePipeline(object):
    def process_item(self, item, spider):
        return item

class SubmitPipeline(object):
    def __init__(self, connect):
        self.connect = connect

    @classmethod
    def from_crawler(cls, spider):
        return cls(
           connect=spider.connect
        )

    def process_item(self, item, spider):
        data_list=[]
        self.connect.submit_data(data_list.append(dict(item)))
        return item


