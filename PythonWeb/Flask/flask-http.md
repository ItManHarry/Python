# Flask Framework HTTP

## Request对象

- 使用request的属性获取请求URL

	url: http://helloflask.com/hello?name=Grey	
	
| 属性 | 值 | 
| ------------- | ------------- | 
| path | '/hello' | 
| full_path | '/hello?name=Grey' |
| host | 'helloflask.com' | 
| host_url | 'http://helloflask.com/' |
| base_url | 'http://helloflask.com/hello' | 
| url | 'http://helloflask.com/hello?name=Grey' |
| url_root | 'http://helloflask.com/' | 

- request对象常用的属性和方法

| 属性/方法 | 说明 | 
| ------------- | ------------- | 
| args | Werkz eug 的ImmutableMultiDict 对象。存储解析后的查询字符串，可通过字典方式获取悦值。如果你想获取未解析的原生查询字符串，可以使用query_s tring属性 | 
| blueprint | 当前蓝本的名称 | 
| cookies | 一个包含所有随请求提交的cookies 的字典 | 
| data | 包含字符串形式的请求数据 | 
| endpoint | 与当前i苛求相匹配的端点值 | 
| files | Werkzeug的MultiDict 对象，包含所有上传文件，可以使用字典的形式获取文件。使用的键为文件input 标签中的name属性值，对应的值为Werkzeug的FileStorage 对象，可以调用save()方法并传入保存路径来保存文件 | 
| form | Werkz e ug 的ImmutableMultiDict 对象。与files 类似，包含解析后的表单数据。表单字段值通过input 标签的name 属性值作为键获取 | 
| values | Werkzeug 的CombinedMultiDict 对象，结合了args 和form 属性的值 | 
| get_data(cache=True, as_text=False,parse_from_data=False | 获取消求中的数据, 默认读取为字节字符串（ bytestring ）， 将as_text 设为True,则返回值将是解码后的unicode 字符串 | 
| get_json(self, force=False,silent=False,cache=True | 作为JSON解析并返回数据，如果MlME 类型不是JSON ，返回None(除非force 设为True ）；解析出错则抛出Werkzeug 提供的BadRequest 异常（ 如果未开silent= False, cache=True) 启调试模式，则返回400错误响应，后面会详细介绍）, 如果silent 设为True 则返回None; cache 设置是否缓存解析后的JSON 数据 | 
| headers | 一个Werkzeug 的EnvironHeaders 对象，包含首部字段， 可以以字典的形式操作 | 
| is_json | 通过MIME 类型判断是否为JSON 数据，返回布尔值 | 
| json |  包含解析后的JSON 数据，内部调用getjso n （），可通过字典的方式获取键值 | 
| method | 请求的HTTP 方法 |
| method | 请求发起的源URL ， 即referer |
| scheme | 请求的U RL 模式（ http 或https ) |
| user_agent | 用户代理（ UserAgent, UA ） ，包含了用户的客户端类型，操作系统类型等信息 |