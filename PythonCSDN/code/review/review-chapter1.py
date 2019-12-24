#Review
#变量 - 变量无需声明，可直接使用
print('-' * 80)
a = 100
b = 'Python'
c = 3.14
print('a is : ', a, ', b is : ' , b, ', c is : ',c)
print('-' * 80)
#字符串
#字符串可以包含任意字符，可用单引号也可用双引号
v_str1 = "Harry is studying Python, keep going."
print(v_str1)
v_str2 = 'If you want to change , just do it. And you should never stop.'
print(v_str2)
print('-' * 80)
#字符串使用“+”拼接，拼接非字符串需要使用str()或者repr()函数转换后再拼接
v_str3 = "Hello , who are you ?\t"
v_str4 = "Hello, I am Harry.\t"
v_str5 = "How old are you ? \t"
v_age = 36
v_str6 = "I am " + str(v_age) + ' years old.'
print(v_str3 + v_str4)
print(v_str5 + v_str6)
print('-' * 80)
#长字符串
v_str7 = '''
    Long long ago , there was a boy,
    His name is Jack.
    He liked to study.
    ...
'''
print(v_str7)
print('-' * 80)
v_rstr = r'This is a resource string, \t will not be a table'
print(v_rstr)
print('-' * 80)
#转义字符
v_str = "abc\bdef\nghi\rjkl\tmno\"opqr\'stu\\vwxys"
print(v_str)
print('-' * 80)
#字符串转字节串
v_bytes = b'IamHarry'
print(type(v_bytes))
print('bytes array\'s length is : ', len(v_bytes))
for b in v_bytes:
    print(b)
    print('Character : ' + str(b) + '\t')
    print('Character is : %r' %b)
print('-' * 80)
#字符串常用函数
#索引计算字符串
v_str = "abcdefghijklmnopqistuvwxyz"
print(v_str[3:6])
print(v_str[8])
print(v_str[-8:-1])
print(v_str[1:10:3])
print('-' * 80)
#in判断是否包含某个字符
print('a is in the string : ', 'a' in v_str)
print('2 is in the string : ', '2' in v_str)
print('-' * 80)
#len()字符串长度
print('v_str length is : ', len(v_str))
print('-' * 80)
#max/min函数
print("Max character : ", max(v_str))
print("Min character : ", min(v_str))
print('-' * 80)
#title()首字母大写
print(v_str.title())
print('-' * 80)
#upper()全部大写
print(v_str.upper())
print('-' * 80)
#lower()全部小写
print(v_str.lower())
print('-' * 80)
#strip()去除空格
print(v_str.strip())
print('-' * 80)
#startswith()是否以某个字符开头
print(v_str.startswith('b'))
print('-' * 80)
#endswith()是否以某个字符结尾
print(v_str.endswith('z'))
print('-' * 80)
#find()查找字符，存在返回index，不存在返回-1
v_index = v_str.find('g')
print('Index is : ', v_index)
v_index = v_str.find('8')
print('Index is : ', v_index)
print('-' * 80)
#replace()替换字符
v_new_str = v_str.replace('abc', '123')
print('New string is : ', v_new_str)
print('-' * 80)
#split()分割字符串
v_str = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q'
v_array = v_str.split(',')
print(v_array)
print('-' * 80)
#join()连接字符串
v_str = '-'.join(v_array)
print('Now the string is : ', v_str)
print('-' * 80)
#运算符
x = 20
y = 7
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x ** 2)
print('-' * 80)
x += 100
print(r'x+=100 :', x)
x -= 10
print(r'x-=10 :', x)
x *= 2
print(r'x*=2 :', x)
x /= 4
print(r'x/=4 :', x)
x //= 5
print(r'x//=5 :', x)
x %= 4
print(r'x%=4 :', x)
x **= 3
print(r'x**=3 :', x)
print('-' * 80)
x , y = 20, 30
print('x : ', x, ' y : ', y)
print(r'x > y : ', x > y)
print(r'x >= y : ', x >= y)
print(r'x < y : ', x < y)
print(r'x <= y : ', x > y)
print(r'x == y : ', x == y)
print(r'x != y : ', x != y)
z = x
print('z : ', z)
print(r'z is x : ', z is x)
print(r'z is not x : ', z is not x)
b1,b2 = True, False
print('b1 : ', b1, ' b2 : ', b2)
print('b1 and b2 : ', b1 and b2)
print('b1 or b2 : ', b1 or b2)
print('not b1 : ', not b1)
print('not b2 : ', not b2)
print('-' * 80)
#三目运算符
#表达式：True_Statements if expression else Else_Statements，支持嵌套
print('I am OK!' if b2 else print('I am OK indeed!') if b1 else print('I am not OK!'))
print('-' * 80)