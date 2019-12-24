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