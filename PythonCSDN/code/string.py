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
#字符串不能和非字符串通过加好进行拼接
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
#字符串转字节串 方式一:使用bytes()函数
b2 = bytes('abc', 'utf-8')
print(b2)
#字符串转字节串 方式一:使用encode()函数
b3 = "I Love You".encode()
print(b3)
#使用decode将bytes解码成字符串
s = b3.decode('utf-8')
print(s)