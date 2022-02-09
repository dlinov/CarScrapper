# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarscrapperItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    price_usd = scrapy.Field()
    price_eur = scrapy.Field()
    img = scrapy.Field()

    
