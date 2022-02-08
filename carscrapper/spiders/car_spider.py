import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from ..items import CarscrapperItem

class CarsSpider(scrapy.Spider):
    name = "cars"
     # 205 or more for prod, maybe somehow dynamically determine exact number 
    start_urls = list(f"https://ab.onliner.by/?page={page}" for page in range(1, 5))
    
    def __init__(self):
        options = Options()
        options.headless = True 
        self.driver = webdriver.Firefox(options=options)
    
    def parse(self, response):
        item = CarscrapperItem()
        
        self.driver.get(response.url)
        res = response.replace(body=self.driver.page_source)

        for car_div in res.css('.vehicle-form__offers-unit'):
            name = car_div.css('.vehicle-form__link_noreflex::text').extract_first()
            prices = car_div.css('.vehicle-form__offers-part_price').css('.vehicle-form__description.vehicle-form__description_tiny.vehicle-form__description_other::text').extract_first()
            img = car_div.css('.vehicle-form__image::attr(style)').extract_first()

            prices_stripped = list(x.strip() for x in prices.split('/'))
            price_usd = next(filter(lambda p: p.endswith('$'), prices_stripped), None)
            price_eur = next(filter(lambda p: p.endswith('€'), prices_stripped), None)
            
            item['_id'] = response.url.split('/')[-1]
            item['name'] = name.strip()
            item['price_usd'] = price_usd
            item['price_eur'] = price_eur
            item['img'] = img

            yield item


        