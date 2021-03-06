# Chapter 1- Python入门与字符串

## 变量

- Python变量无需提前声明，可以随时声明使用

- Python变量类型可变

### 字符串

- 字符串的基础用法

	1. 字符串可包含任何字符
	
	2. 即可单引号也可双引号	
	

- 字符串拼接

	1. 使用“+”拼接
	
	2. 使用str()或者repr()函数进行转换
	
	3. repr()会以Python表达式的形式来表示值
	
	
- 使用input()向用户生成一条提示，然后获取用户输入内容（Python2使用的是raw_input()）

- 长字符串与原始字符串

	1.  三引号（单双都可以）表示长字符串
	
	2. 原始字符串以r开头，原始字符串不会把反斜线当做成特殊字符
	
	3. 如果原始字符串包含引号，同样需要进行转义

- 字节串和字符串

	1. 字符串有多个字符组成，字节串有多个字节组成
	
	2. 字节串和字符串除了操作的数据单元不同，他们所支持的方法基本相同，字节串也是不可变序列
	
	
	3. 字符串和字节串相互转换（三种方式）
	
		3.1.  如果字符串内容都是ASCII字符，在字符在前面加b前缀即可构建字节串
		
		3.2. 使用bytes()函数将字符串转换为字节串
		
		3.3. 使用encode()函数将字符串转换为字节串
		
		3.4 调用bytes对象的decode()方法将bytes对象解码成字符串
- 字符串的高级用法

	1. 转义字符
	
		\b 退格符
		\n 换行符
		\r 回车符
		\t 制表符
		\\" 双引号
		\\' 单引号
		\\ 反斜线		
	
	2. 字符串格式化
	
		使用%加上转换说明符实现字符串格式化， Python转换说明符如下：
		
			d,i 	转换为带符号的十进制整数
			
			o  	转换为带符号的八进制整数
			
			x,X	转换为带符号的十六进制整数
			
			e,E	转换为科学计数法表示的浮点数
			
			f,F		转换为十进制的浮点数
			
			g		智能选择f或e格式
			
			G 		智能选择F或E格式
			
			C		转换为单字符（只接受整数或单字符字符串）
			
			r		使用repr()将变量或者表达式转换为字符串
			
			s		使用str()将变量或者表达式转换为字符串
	
	3. 调用函数操作字符串
	
		3.1. 基于索引的计算
		
		3.2. in运算
		
		3.3. len()运算
		
		3.4. min()/max()函数
		
		3.5. title()方法：将字符串的首字母大写
		
		3.6. lower() 方法：将字符串小写
		
		3.7. upper()方法：将字符串大写
		
		3.8. strip()方法：去除前后的空格
		
		3.9. lstrip()方法：去除前端的空格
		
		3.10. rstrip()方法：去除后面的空格
		
		3.11. startwith()方法：是否某个字符打头
		
		3.12. endswith()方法：是否某个字符结尾
		
		3.13. find()方法：查找字符是否存在，找到返回index值，否则返回-1
		
		3.14. index() 方法：查找字符是否存在，找到返回index值，否则报ValueError
		
		3.15. replace()方法：使用指定的字符串替换字符串中的目标字符
		
		3.16. translate()方法：使用指定的翻译映射表对字符串进行替换
		
		3.17. split()方法：分割字符串
		
		3.18. join()方法：连接字符串
		
## 运算符

- 赋值运算符及扩展的赋值运算符

	1. “=”赋值	

- 算数运算符

	1. +，-，*，/，//(整除)，%，**
	
	2. 复杂的数学运算需要导入math模块
	
	3. 扩展运算符
	
		3.1. += : x += y(x = x + y)
		3.2 -= : x -= y(x = x - y)
		3.3. *= : x *= y(x = x * y)
		3.4. /= : x /= y(x = x / y)
		3.5. //= : x //= y(x = x // y)
		3.6. %= : x %= y(x = x % y)
		3.7. **= : x **= y(x = x ** y)

- 索引运算符

	1. 索引运算符就是方括号
	
	2. 方括号中可以使用单个索引值，访问单个元素
	
	3. 方括号也可以使用索引范围，还可以设置步长
	
	4. 索引运算符适用于所有的序列（字符串、字节串、列表、元组等）
	
- 比较运算符和逻辑运算符
	
	1. &gt;, &gt;= : 大于，大于等于
	
	2. &lt;, &lt;= : 小于，小于等于
	
	3. == : 等于
	
	4. != : 不等于
	
	5. is(is not) : 判断两个变量的引用对象是否相同（不相同），如果相同（不相同）则返回True， 否则返回False
	
	6. and : 与，任一操作数为False，返回便是False
	
	7. or : 或，任一操作为为True，返回便是True
	
	8. not : 非，操作数为False，返回True，操作数为True，返回False
	
- 三目运算符

	Python用if来代替三目运算符
	
	语法： True_Statements if expression else Else_Statements
	
```python	
	age = 25
	print('age bigger than 25' if age > 25 else print('age less than 25'))
```

	if支持嵌套
	
	
	注：True_Statements可以放置多个语句，如果用“,”号隔开，则返回多个语句返回值组合的元组，如果用“;”号隔开，则返回第一条语句返回的值
	
```python	
	age = 25
	s = print("比25大"), "成年人" if  age > 25 else print('小于或者等于25')
	print(s)
``` 
	
- in运算符

	判断一个元素是否在序列之中