# Flask Framework Form

## 表单

	扩展Flask-WTF 集成了WTForms ，使用它可以在Flask 中更方便地使用WTForms 。FlaskWTF将表单数据解析、CSRF 保护、文件上传等功能与Flask 集成，另外还附加了reCAPTCHA支持。
	
- 安装Flask-WTF

```
	pip install flask-wtf
```

- 常用的WTForms字段

| 字段类 | 说明 | 对应的HTML表示 |
| ---- | ---- | ---- |
| BooleanField | 复选框，值会被处理为True 或False | &lt;input type="checkbox"&gt; |
| DateField | 文本字段，值会被处理为datetime . date 对象 | &lt;input type = "text"&gt; |
| DateTimeField | 文本字段，值会被处理为datetime.datetime对象| &lt;input type = "text"&gt; |
| FileField | 文件上传字段 | &lt;input type = "file"&gt; |
| FloatField | 浮点数字段，值会被处理为浮点型 | &lt;input type = "text"&gt; |
| IntegerField | 整数字段，值会被处理为整型 | &lt;input type = "text"&gt; |
| RadioField | 一组单选按钮 | &lt;input type = "radio"&gt; |
| SelectField | 下拉列表 | &lt;select&gt;&lt;option&gt;&lt;/option&gt;&lt;\/select&gt; |
| SelectMultipleField | 多选下拉列表 | &lt;select multiple&gt;&lt;option&gt;&lt;/option&gt;&lt;/select&gt; |
| SubmitField | 提交按钮 | &lt;input type = "submit"&gt; |
| Stringfield | 文本字段 | &lt;input type = "text"&gt; |
| HiddenField | 隐藏文本字段 | &lt;input type = "hidden"&gt; |
| PasswordField | 密码文本字段 | &lt;input type = "password"&gt; |
| TextAreaField | 多行文本字段 | &lt;textarea>&lt;\/textarea&gt; |

- 实例化字段类常用参数

| 参数 | 说明 |
| ---- | ---- |
| label | 字段标签&lt;label&gt;的值，也就是渲染后显示在输入字段前的文字 |
| render_kw | 一个字典，用来设置对应的HTML &lt;input&gt;标签的属性，比如传入{'placeholder':'YourName'｝，渲染后的HTML 代码会将&lt;input&gt;标签的placeholder属性设为Your Name|
| validators | 一个列表，包含一系列验证器，会在表单提交后被逐一调用验证表单数据 |
| default | 字符串或可调用对象，用来为表单字段设置默认值 |

- 常用的WT Form s 验证器

| 验证器 | 说明 |
| ---- | ---- |
| DataRequired(message=None)| 验证数据是否有效 |
| Email(message=None) | 验证Emai l 地址 |
| EqualTo(fieldname, message＝None) | 验证两个字段值是否相同 |
| InputRequired(message=None)| 验证是否有数据 |
| Length(min=-1 , max=-1 , message=None) | 验证输入值长度是否在给定范围内 |
| NumberRange(min=None, max=None, message=None) | 验证输入数字是否在给定范围内 |
| Optional(strip_whitespace=True) | 允许输入值为空， 并跳过其他验证 |
| Regexp(regex, flags=0, message=None） | 使用正则表达式验证输入值 |
| URL(require_tld=True , message=None) | 验证URL |
| AnyOf( values, message=None, values_formatter= None) | 确保输入值在可选值列表中 |
| NoneOf(values, message=None, values_formatter=None) | 确保输入值不在可选值列表中 |

```python
	f rom flask_wtf import FlaskForm
	from wtforms import StringField, PasswordField, BooleanField , SubmitField
	from wtforms.validators import DataRequired, Length
	class LoginForm(FlaskForm):
		username = StringField ( 'Username ', validators=[ DataRequired() ] )
		pas sword= PasswordField( 'Password', validators= [DataRequired() , Length (8 , 128)])
		remember = BooleanField('Remember me ')
		submit = SubmitField ( 'Login')
```

默认情况下， WTForms 输出的字段HTML 代码只会包含id 和name 属性，属性值均为表单类中对应的字段属性名称。如果要添加额外的属性，通常有两种方法:

	1. 使用render_kw 属性
	
```python
	username = StringField('Username', render_kw={'placeholder ':'Your Username'})
```
	输入的html代码：
	
```html
	<input type ="text" id="username" name="username" placeholder="Your Username">
```

	2. 在调用宇段时传入
	
```html
	{{ form.body.label(class='form-label')}}
    {{ form.body(class='form-control',placeholder='请输入消息',row='3')}}
```

## 验证表单数据

- 客户端验证

	使用前端js框架完成验证即可
	
- 服务器验证

	WTForms 验证表单字段的方式是在实例化表单类时传人表单数据，然后对表单实例调用validate()方法。这会逐个对字段调用字段实例化时定义的验证器，返回
表示验证结果的布尔值。如果验证失败，就把错误消息存储到表单实例的errors 属性对应的字典中。

```python
	from flask import request
	@app.route ('/basic',methods=[ 'GET','POST' ])
	def basic() :
		form = LoginForm() # GET + POST
		if request.method == 'POST' and form.validate() :
				＃处理POST 请求
		return render_template( ' forms/basic.html ', form=form) ＃处理GET 请求
```

	Flask-WTF 提供的validate_on_submit() 方法合并了这两个操作，因此上面的代码可以简化为：
	
```python
	from flask import request
	@app.route ('/basic',methods=[ 'GET','POST' ])
	def basic() :
		form = LoginForm() # GET + POST
		if form.validate_on_submit() :
				＃处理POST 请求
		return render_template( 'forms/basic.html',form=form) ＃处理GET 请求
```

- 在模板中渲染错误消息

	如果form.validate_on_submit()返回False,那么说明验证没有通过。对于验证未通过的字段， WTForms会把错误消息添加到表单类的errors 属性中，这是
一个匹配作为表单字段的类属性到对应的错误消息列表的字典。我们一般会直接通过字段名来获取对应字段的错误消息列表，即"form.字段名.errors" 。
比如， form.name.errors 返回name 字段的错误消息列表。

```html
	<form method="post">
		{{ form.csrf token }}
		{{ form.username.label }} <b r>
		{{ form.username()}} <br>
		{%for message in form.username.errors %｝
			<small class="error"> {{ message }} </small><br>
		{%endfor %｝
		{{ form.password.label }}<br>
		{{ form.password }} <br>
		{%for message in form.password.errors %}
			<small class="error"> {{ message }} </ small><br>
		{ %endfor %｝
		{{ form.remember }}{{ form.remember.label }}< br>
		{{ form.submit }}<br>
	</form>
```

- 自定义验证器

	1. 行内验证器
	
```python
	from wtforms import IntegerField , SubmitField
	from wtforms.validators import ValidationError
	class FortyTwoForm (FlaskForm ) :
		answer = IntegerField ('The Number')
		submit = SubmitField ()
		def validate_answer(form , field ):
			if field.data ! = 42 :
				raise ValidationError ( 'Must be 42.')
```

	2. 全局验证器
	
```python
	def is_admin(message=None):
    if message is None:
        message = '请输入管理员账号'
    def _is_admin(form, field):
        if field.data != 'admin':
            raise ValidationError(message)
    return _is_admin
	class LoginForm(BaseForm):
    '''
        字段名称大小写敏感，不能以下划线或validate开头
        注：即使用全局校验器又使用了行内校验器的情况，两个校验器均生效
    '''
    username = StringField('User Name',validators=[DataRequired(),InputRequired('Please Input User Name!'),is_admin('账号为非管理员账号,请更正!')])
    password = PasswordField('Password',validators=[DataRequired(),Length(8,128),InputRequired('Please Input Password!'),validate_adminpwd])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
```	

