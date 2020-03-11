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
	scrapy shell -s USER-AGENT='Mozilla/5.0' https://www.zhipin.com/guangzhou/?ka=city-sites-101280100
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
		@								匹配属性
	
	
	
