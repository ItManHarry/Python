#list and tuple
order_ending = ('st','nd','rd') + ('th',) * 17 + ('st','nd','rd') + ('th',) * 7 + ('st',)
print(order_ending)
day = input('Input a date(1-31): ')
print(day + order_ending[int(day) -1])
#list methods - sort
v_list = ['Harry','Jack','A','Sam','Henry','BBBBBB','DDDDDDDDD', 'CC']
#key代表len函数排序 ， reverse为True表示降序排序
v_list.sort(key=len,reverse=True)
print(v_list)
#字典格式化字符串
v_info = dict(name='Harry',age=37)
v_str = 'I am %(name)s, and I am %(age)d years old.'
print(v_str %v_info)
for k, v in v_info.items():
    print('Key is : ', k, ' Value is : ', v)