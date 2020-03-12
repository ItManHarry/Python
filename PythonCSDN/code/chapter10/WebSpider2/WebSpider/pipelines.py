# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class WebspiderPipeline(object):

    def __init__(self):
        self.db_conn = sqlite3.connect('jobs.db')
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute("""
            create table if not exists tb_job(
                id integer primary key autoincrement,
                title,
                salary,
                workplace
            )
        """)

    #该方法中的item就是yield的item对象
    def process_item(self, item, spider):
        print('工作名称 : ', item['title'])
        print('工资 : ', item['salary'])
        print('工作地点 : ', item['workplace'])
        self.db_cursor.execute('insert into tb_job(title, salary, workplace) values(?,?,?)', (item['title'], item['salary'], item['workplace']))
        self.db_conn.commit()
    #关闭爬虫    
    def close_spider(self, spider):
        print('-------------------------------- close the db connection -------------------------------- ')       
        self.db_cursor.close()
        self.db_conn.close()