import urllib.request as ur
import urllib.parse as up
#urlopen(url, data=None):打开url对应的资源
#GET请求 参数直接放到url地址后面即可
params = {'y':2019,'m':12}
with ur.urlopen('http://10.41.129.35/esb/scb/funnel/bonus/getData.do?%s' %up.urlencode(params)) as f:
    print(f.read().decode('UTF-8'))
#POST请求使用data传入产生
print('-' * 190)
params = {'p1':300,'p2':400}
with ur.urlopen('http://localhost:8080/esb/test/rep/post.do',data=up.urlencode(params).encode('utf-8')) as f:
    print(f.read().decode('UTF-8'))
params = {'p1':300,'p2':400}
req = ur.Request(url='http://localhost:8080/esb/test/rep/post.do?%s' %up.urlencode(params) ,method='POST')
with ur.urlopen(req) as f:
    print(f.read().decode('UTF-8'))
print('-' * 190)  
#如果需要发送PUT\PATCH\DELETE等请求，需要创建Request对象
params = {'p1':100,'p2':200}
req = ur.Request(url='http://localhost:8080/esb/test/rep/put.do?%s' %up.urlencode(params) ,method='PUT')
#req = ur.Request(url='http://localhost:8080/esb/test/rep/put.do', data=up.urlencode(params).encode('utf-8')  ,method='PUT')
with ur.urlopen(req) as f:
    print(f.read().decode('UTF-8'))
print('-' * 190)   