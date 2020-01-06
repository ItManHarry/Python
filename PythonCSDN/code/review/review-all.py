print('-' * 80)
name = 'ChengGuoqian'
age = 36
email = 'guoqian.cheng@doosan.com'
info = 'Name:\t'+name+'\tage:\t'+str(age)+'\temail:\t'+email
print(info)
print('-' * 80)
r_str = r'This is a resource string , \t\b\n will be OK!'
print(r_str)
print('-' * 80)
bytes = b'thisisastringforbytes'
print('Bytes type is : \t', type(bytes))
print('Length of the bythes : \t', len(bytes))
for b in bytes:
    print('Bythe : \t', str(b))
print('-' * 80)
v_str = 'abcdefghijklmnopqrstuvwxyz'
print(v_str[1:10])
print('a is in the string : \t','a' in v_str)
print('2 is in the string : \t','2' in v_str)
print('-' * 80)