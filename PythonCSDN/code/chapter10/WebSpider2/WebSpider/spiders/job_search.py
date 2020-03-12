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