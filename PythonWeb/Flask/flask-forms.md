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