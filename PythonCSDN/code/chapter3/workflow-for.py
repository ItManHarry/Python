#程序流程 - 循环
#while
v_list = [1,2,3,4,5,3,3,4,5,2,9,8,10]
v_dict = {'A':100,'B':200,'C':300,'D':400}
print(len(v_list))
print('-' * 80)
i = 0
while i < len(v_list):
    print(v_list[i])
    i += 1
print('-' * 80)
i = 0
v_keys = list(v_dict.keys())
while i < len(v_keys):
    print('Key : ', v_keys[i], ', Value : ', v_dict[v_keys[i]])
    i += 1
#for循环
print('-' * 80)
for i in v_list:
    print(i)
print('-' * 80)
for k, v in v_dict.items():
    print('Key : ', k, ', Value : ', v)
print('-' * 80)
for i in range(10):
    print(i)
else:
    print('loop over')
print('' * 80)
for i in range(10):
    j = 0
    while j < 20:
        print("i is : %d, j is : %d" %(i, j))
        j += 1
