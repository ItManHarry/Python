from collections import OrderedDict
print('-' * 80)
dx = OrderedDict(b=5,c=3,a=6)
print(dx)
print('-' * 80)
dx = OrderedDict()
dx['a'] = 100
dx['t'] = 300
dx['e'] = 490
dx['c'] = 590
for k,v in dx.items():
    print('Key is : ', k, ' ,Value is : ', v)
print('-' * 80)