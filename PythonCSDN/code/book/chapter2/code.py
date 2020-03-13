#单行注释
'''
    这是多行
    注释，编译会忽略
'''
"""
     这也是多行
    注释，编译会忽略
"""
#整型
n = 9999999999999999
print('n type is : ', type(n))
#Python3.X允许为数值（包括浮点型）增加下划线作为分隔符
n = 1_000_000
print('n is : ',n)
n = 234_234_234
print('n is : ', n)
'''
    浮点型 - 包含两种形式
    1. 十进制：浮点数必须包含小数点，否则会被当做整数处理
    2. 科学计算形式：5.12e2(或者5.12E2)即5.12 * 10的2次方
'''
n = 4.12e2
print('n type is : ', type(n))
print(n)
n = 8e3
print(n)
#原始字符串(结尾的反斜线需单独写)
rstr = r'd:\github\abc\d' '\\'
print(rstr)
#字符串和字节串
#字符串 -> 字节串 方法一：直接加b
b = b'abc'
print(type(b), ' value is : ', b)
#字符串 -> 字节串 方法二：调用bytes方法进行转换
b = bytes('我爱Python','utf-8')
print(type(b), ' value is : ', b)
#字符串 -> 字节串 方法三：调用字符串的encode方法进行转换
b = '我爱Python'.encode('utf-8')
print(type(b), ' value is : ', b)
#字节串 -> 字符串 ：调用字节串的decode方法
s = b.decode('utf-8')
print(s)