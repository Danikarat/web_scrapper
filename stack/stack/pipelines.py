# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

from scrapy.exceptions import DropItem
import logging
 


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(meassage)s',
    level=logging.INFO
)


class StackPipeline:
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
    
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
                settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        
    
    def from_crawler(cls,crawler):
        # This method is used to get settings from the crawler
        pipeline = cls()
        pipeline.settings = crawler.settings 
        return pipeline
        
        
        
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            # logging.info("Question added to MongoDB database!",
            #         level=log.DEBUG, spider=spider)
            logging.debug(f"Queetion added to MongoDB database by {spider.name} spider")
        return item