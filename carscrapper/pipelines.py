# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import time
from datetime import datetime

class CarscrapperPipeline(object):
    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['cars']
        self.collection = db['cars_tb']
    
    def process_item(self, item, spider):
        ts = time.time()
        item['ts'] = datetime.utcfromtimestamp(ts)
        img = item['img']
        img = img.replace('");', '')
        img = img.replace('background-image: url("', '')
        item['img'] = img
        obj = dict(item)
        id = obj.pop('_id')
        # TODO: update only if contents differ
        self.collection.update({'_id': id}, {'$push': {'versions': obj}})
        return item
