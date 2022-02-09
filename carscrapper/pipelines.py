# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from datetime import datetime

class CarscrapperPipeline(object):
    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['cars']
        self.collection = db['scraped_data']
    
    def process_item(self, item, spider):
        ts = datetime.isoformat(datetime.now())
        # print(f'=== Processing {item} at {ts}')
        cars = self.collection
        img = item['img']
        img = img.replace('");', '')
        img = img.replace('background-image: url("', '')
        item['img'] = img
        obj = dict(item)
        id = obj['url'].split('/')[-1]
        existing = cars.find_one(id)
        # print(f'=== Car {id}: {existing}')
        if existing:
            prev_state = existing['versions'][-1]
            # update only if contents differ
            # TODO: check if comparison works as expected
            # print(f'=== Comparing car {id}: {prev_state} and {obj}')
            if obj != prev_state:
                cars.update_one({'_id': id}, {'$push': {'versions': {'ts': ts, 'state': obj}}})
        else:
            cars.insert_one({'_id': id, 'versions': [{'ts': ts, 'state': obj}]})
        return item
