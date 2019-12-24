#string
s1 = "Hello ' Python"
print("String1 is : ", s1)
s2 = 'Hello\' Python'
print("String2 is : ", s2)
s1 = "Hello"
s2 = " World"
s3 = s1 + s2
print("String3 is : " , s3)
n = 2.3
#字符串不能和非字符串通过加号进行拼接
#s4 = s3 + n
#print("String4 is : " , s4)
#可以通过str()或者repr()函数进行转换
s4 = s3 + str(n)
print("String4 is : " , s4)
s5 = s3 + repr(n)
print("String5 is : " , s5)
s6 = "Python"
print(repr(s6))
s = input("请输入......")
print(s)
#三引号
s = '''
    I am Harry, 
    I am studying the Python now.
'''
print(s)
#原始字符串
rs = r'我在学习\'Python\'\n,你在干什么？'
print(rs)
#字符串转字节串 方式一:加b前缀
b1 = b'abc'
print(type(b1))
#字符串转字节串 方式二:使用bytes()函数
b2 = bytes('abc', 'utf-8')
print(b2)
#字符串转字节串 方式三:使用encode()函数
b3 = "I Love You".encode()
print(b3)
#使用decode将bytes解码成字符串
s = b3.decode('utf-8')
print(s)
#字符串高级
s = "a\tb\tc"
print(s)
s = "I love %s"
print(s % "Python")
s = "I love %s, the price is %d"
print(s%("Python book",300))
price = 128
s = "price is :%d, o value is : %o, x value is : %x, string value is : %r "
print(s%(price,price,price,price))
#字符串索引
s = "IamChengGuoqian"
print(s[2])
print(s[2:6])
print(s[2:7:2])
#in是否包含
print('hdd' in s)
#字符串长度
print(len(s))
#取最大最小字符
print(max(s), min(s))
#title函数
s = "abCDEfg"
print(s.title())
print(s.lower())
print(s.upper())
s = "   Python  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
s = 'IamHarry'
print(s.startswith('I'))
print(s.endswith('a'))
print(s.find('m'))
print(s.find('v'))
print(s.index('H'))
#print(s.index('v'))
s = s.replace('a', 'v')
print(s)
print(s.find('v'))
#print(s.translate())
s = "a.b.c.d.e"
print(s.split("."))
print("|".join(s.split(".")))