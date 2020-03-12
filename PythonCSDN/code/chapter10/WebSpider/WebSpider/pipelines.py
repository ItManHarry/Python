# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class WebspiderPipeline(object):

    def __init__(self):
        self.json_file = open('jobs.json','wb+')
        self.json_file.write('[\n'.encode('utf-8'))

    #该方法中的item就是yield的item对象
    def process_item(self, item, spider):
        print('工作名称 : ', item['title'])
        print('工资 : ', item['salary'])
        print('工作地点 : ', item['workplace'])
        text = json.dumps(dict(item), ensure_ascii = False) + ',\n'
        self.json_file.write(text.encode('utf-8'))
    #关闭爬虫    
    def close_spider(self, spider):
        print('-------------------------------- close the json file -------------------------------- ')
        self.json_file.seek(-2, 1)
        self.json_file.write('\n]'.encode('utf-8'))
        self.json_file.close()