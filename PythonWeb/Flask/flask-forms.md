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
| BooleanField | 复选框，值会被处理为True 或False | <input type="checkbox"> |
| DateField | 文本字段，值会被处理为datetime . date 对象 | <input type = "text"> |
| DateTimeField | 文本字段，值会被处理为datetime.datetime对象| <input type = "text"> |
| FileField | 文件上传字段 | <input type = "file"> |
| FloatField | 浮点数字段，值会被处理为浮点型 | <input type = "text"> |
| IntegerField | 整数字段，值会被处理为整型 | <input type = "text"> |
| RadioField | 一组单选按钮 | <input type = "radio"> |
| SelectField | 下拉列表 | <select><option><\/option><\/select> |
| SelectMultipleField | 多选下拉列表 | <select multiple><option><\/option><\/select> |
| SubmitField | 提交按钮 | <input type = "submit"> |
| Stringfield | 文本字段 | <input type = "text"> |
| HiddenField | 隐藏文本字段 | <input type = "hidden"> |
| PasswordField | 密码文本字段 | <input type = "password"> |
| TextAreaField | 多行文本字段 | <textarea><\/textarea> |