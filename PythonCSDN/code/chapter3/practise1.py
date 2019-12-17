#打印菱形1
N = 20
v_list = list(range(N))
print(v_list)
for i in v_list:   
    print(' ' * (N-i), '*'*(i*2+1))        
v_list.reverse()
for i in v_list:
    if i == N - 1:
        continue
    print(' ' * (N-i), '*'*(i*2+1))
print('-' *80)
#乘方开方
a = 27
print(a ** 2)
print(a ** (1/3))
print('-' *80)
#打印菱形2
N = 9
v_fs = list(range(N))
for i in v_fs:
    if i == 0:
        print(' ' * (N - 1 - i) +'*')
    else:
        print(' ' * (N - 1 - i)+'*'+ ' ' * (i *2 -1)+'*')
v_fs.reverse()
for i in v_fs:
    if i == N - 1:
        continue
    elif i == 0:
         print(' ' * (N - 1 - i) +'*')
    else:
        print(' ' * (N - 1 - i)+'*'+ ' ' * (i *2 -1)+'*')