# Python爬虫

## 下载安装Scrapy

	1. 首先安装Twisted
	
		1.1. 登录https://www.lfd.uci.edu/~gohlke/pythonlibs/网址
		1.2. 现在对于的whl文件
		1.3. 运行cmd，cd到下载的whl文件路径执行：pip install Twisted-19.10.0-cp38-cp38-win_amd64.whl 命令即可
	
	2. 安装Scrapy
	
		2.1. 运行cmd执行：pip install scrapy 命令即可
		
## 创建Scrapy项目

	使用命令：scrapy startproject [project name] 创建Scrapy项目
	
## Scrapy核心组件

	1. 调度器：该组件由Scrapy框架实现
	
	2. 下载器：该组件由Scrapy框架实现
	
	3. 蜘蛛：该组件有开发者实现
	
	4. Pipeline：该组件有开发者实现
	
##  	使用Shell调试

	1. 启动shell调试抓取数据
	
		首先要查看网页的源代码
		
		命令：scrapy shell 目标网址
		
```
	scrapy shell https://www.zhipin.com/guangzhou/?ka=city-sites-101280100
```		

	如果目标页面返回403， 那就表明对方网站做个反爬虫处理。
	通常的处理方法：
		
		1.1. 浏览器伪装
		
```
	scrapy shell -s USER-AGENT='Mozilla/5.0' https://www.zhipin.com/job_detail/?query=&city=101010100&industry=&position=
```				
		
		1.2. 模拟登陆
	
	2. 使用XPath、CSS选择器提取数据
	
		response.xpath(params)
		
		表达式							作用
		nodename				匹配此节点的所有内容
		/									匹配根节点
		//									匹配任意位置节点
		.									匹配当前节点
		..									匹配父节点
		@								匹配属性
	
## 开发Scrapy项目

- 编写Item

```python
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
		#公司
		company = scrapy.Field()
		#工作地点
		workplace = scrapy.Field()
		#行业    
		industry = scrapy.Field()
		#公司规模
		size = scrapy.Field()
```

- 生成spider

	在Scrapy的spider目录下，执行如下命令：
	
```
	scrapy genspider job_search "zhipin.com"
```

	编写spider:
	
```python
	# -*- coding: utf-8 -*-
import scrapy
from WebSpider.items import WebspiderItem
class JobSearchSpider(scrapy.Spider):
    #爬虫名称
    name = 'job_search'
    #爬取域名
    allowed_domains = ['zhiping.com']
    #爬取起始页面
    start_urls = ['https://www.zhipin.com/beijing/?ka=city-sites-101010100']    

    #该response就代码Scrapy下载器所获取的目标的响应
    #和shell中的response完全一样
    def parse(self, response):
        #所有的工作清单        
        for job_primary in response.xpath('//div[@class="common-tab-box merge-city-job"]/ul[@class="cur"]/li'):           
            #为每个工作创建一个Item
            item = WebspiderItem()
            #工作主信息
            info_primary = job_primary.xpath('./div[@class="sub-li"]')
            item['title'] = info_primary.xpath('./a[@class="job-info"]/p[@class="name"]/span[@class="name-text"]/text()').extract_first()
            item['salary'] = info_primary.xpath('./a[@class="job-info"]/p[@class="salary"]/text()').extract_first() 
            company_info = info_primary.xpath('./a[@class="job-info"]/p[@class="job-text"]/text()').extract()
            if company_info and len(company_info) > 0:
                item['workplace'] = company_info[0]            
            #返回对应的item生成器
            yield item
        for job_primary in response.xpath('//div[@class="common-tab-box merge-city-job"]/ul[@class=""]/li'):           
            #为每个工作创建一个Item
            item = WebspiderItem()
            #工作主信息
            info_primary = job_primary.xpath('./div[@class="sub-li"]')
            item['title'] = info_primary.xpath('./a[@class="job-info"]/p[@class="name"]/span[@class="name-text"]/text()').extract_first()
            item['salary'] = info_primary.xpath('./a[@class="job-info"]/p[@class="salary"]/text()').extract_first() 
            company_info = info_primary.xpath('./a[@class="job-info"]/p[@class="job-text"]/text()').extract()
            if company_info and len(company_info) > 0:
                item['workplace'] = company_info[0]            
            #返回对应的item生成器
            yield item
```

- 编写pielines：

```python
	# -*- coding: utf-8 -*-

	# Define your item pipelines here
	#
	# Don't forget to add your pipeline to the ITEM_PIPELINES setting
	# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


	class WebspiderPipeline(object):
		#该方法中的item就是yield的item对象
		def process_item(self, item, spider):
			print('工作名称 : ', item['title'])
			print('工资 : ', item['salary'])
			print('公司 : ', item['company'])
			print('工作地点 : ', item['workplace'])
			print('行业 : ', item['industry'])
			print('公司规模 : ', item['size'])
```

- 修改settings：

```python
	# -*- coding: utf-8 -*-

	# Scrapy settings for WebSpider project
	#
	# For simplicity, this file contains only settings considered important or
	# commonly used. You can find more settings consulting the documentation:
	#
	#     https://docs.scrapy.org/en/latest/topics/settings.html
	#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
	#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

	BOT_NAME = 'WebSpider'

	SPIDER_MODULES = ['WebSpider.spiders']
	NEWSPIDER_MODULE = 'WebSpider.spiders'


	# Crawl responsibly by identifying yourself (and your website) on the user-agent
	#USER_AGENT = 'WebSpider (+http://www.yourdomain.com)'

	# Obey robots.txt rules
	ROBOTSTXT_OBEY = True

	# Configure maximum concurrent requests performed by Scrapy (default: 16)
	#CONCURRENT_REQUESTS = 32

	# Configure a delay for requests for the same website (default: 0)
	# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
	# See also autothrottle settings and docs
	#DOWNLOAD_DELAY = 3
	# The download delay setting will honor only one of:
	#CONCURRENT_REQUESTS_PER_DOMAIN = 16
	#CONCURRENT_REQUESTS_PER_IP = 16

	# Disable cookies (enabled by default)
	#COOKIES_ENABLED = False

	# Disable Telnet Console (enabled by default)
	#TELNETCONSOLE_ENABLED = False

	# Override the default request headers:
	DEFAULT_REQUEST_HEADERS = {
		'User-Agent':'Mozilla/5.0',
	   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
	}

	# Enable or disable spider middlewares
	# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
	#SPIDER_MIDDLEWARES = {
	#    'WebSpider.middlewares.WebspiderSpiderMiddleware': 543,
	#}

	# Enable or disable downloader middlewares
	# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
	#DOWNLOADER_MIDDLEWARES = {
	#    'WebSpider.middlewares.WebspiderDownloaderMiddleware': 543,
	#}

	# Enable or disable extensions
	# See https://docs.scrapy.org/en/latest/topics/extensions.html
	#EXTENSIONS = {
	#    'scrapy.extensions.telnet.TelnetConsole': None,
	#}

	# Configure item pipelines
	# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
	ITEM_PIPELINES = {
		'WebSpider.pipelines.WebspiderPipeline': 300,
	}

	# Enable and configure the AutoThrottle extension (disabled by default)
	# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
	#AUTOTHROTTLE_ENABLED = True
	# The initial download delay
	#AUTOTHROTTLE_START_DELAY = 5
	# The maximum download delay to be set in case of high latencies
	#AUTOTHROTTLE_MAX_DELAY = 60
	# The average number of requests Scrapy should be sending in parallel to
	# each remote server
	#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
	# Enable showing throttling stats for every response received:
	#AUTOTHROTTLE_DEBUG = False

	# Enable and configure HTTP caching (disabled by default)
	# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
	#HTTPCACHE_ENABLED = True
	#HTTPCACHE_EXPIRATION_SECS = 0
	#HTTPCACHE_DIR = 'httpcache'
	#HTTPCACHE_IGNORE_HTTP_CODES = []
	#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

```

- 执行爬虫命令：

```
	scrapy crawl job_search
```

- 数据写入json文件 - 只修改pipeline文件即可

```python
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
```

- 数据写入数据库

```python
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
```