#URL解析
import urllib.parse
#urlparse()：解析URL字符串，将URL字符串解析成各部分，返回值为ParseResult(tuple子类)
#urlunparse():将URL各个部分(ParseReuslt或tuple)恢复成URL字符串
print('*' * 120)
url = "http://baidu.com/index.html;abc?name=aaa#myflags"
r = urllib.parse.urlparse(url)
print(r)
print('协议 ：', r.scheme, r[0])
print('位置 ：', r.netloc, r[1])
print('路径 ：', r.path, r[2])
print('参数 ： ', r.params, r[3])
print('查询字符串 ：', r.query, r[4])
print('片段 ：', r.fragment, r[5])
print('*' * 120)
e = ('https','www.baidu.com:8080','/index.html','haha','name=Harry','frag')
print(urllib.parse.urlunparse(e))
print('*' * 120)
#查询字符串格式： key=value,多个值用&隔开
qs = "name=Harry&name=Jack&age=37&height=170"
print(urllib.parse.parse_qs(qs))
print(urllib.parse.parse_qsl(qs))
print('*' * 120)
l = [('name','Sam'),('name','Tom'),('age',36),('height', 170)]
print(urllib.parse.urlencode(l))
d = {'name':'Harry','age':36,'height':170,'name':'Henry'}
print(urllib.parse.urlencode(d))
print('*' * 120)