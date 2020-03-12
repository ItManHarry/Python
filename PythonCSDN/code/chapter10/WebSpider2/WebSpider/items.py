# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
class WebspiderItem(scrapy.Item):
    # 工作名称
    title = scrapy.Field()
    #工资
    salary = scrapy.Field()   
    #工作地点
    workplace = scrapy.Field() 