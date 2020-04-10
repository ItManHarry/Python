import time
print('-' * 80)
#显示时区
print(time.tzname)
print('-' * 80)
#当前时间转换为字符串
now_str = time.asctime()
print('Now is : ', now_str)
print('-' * 80)
#将指定的时间（使用包含9个元素的元组表示时间）转换为字符串
time_str = time.asctime((2019,11,2,12,5,35,0,0,0))
print('Time is : ', time_str)
print('-' * 80)
#将以秒代表的时间转换为字符串
time_str = time.ctime(9000000000.0)
print('Time is : ', time_str)
print('-' * 80)
#将当前时间转换为struct_time对象
st = time.gmtime()
print('Now the struct time is : ', st)
print('-' * 80)
#将以秒代表的时间转换为struct_time对象
st = time.gmtime(300)
print('Second time struct time is : ', st)
print('-' * 80)
#将以秒代表的时间转换为代表当前时间的struct_time对象
st = time.localtime(300)
print('Second local time struct time is : ', st)
print('-' * 80)
#将元组代表的时间转换为秒数代表的时间
mt = time.mktime((2019,11,2,12,5,35,0,0,0))
print('Seconds are : ', mt)
print('-' * 80)
#性能计数器的值
count = time.perf_counter()
print('Count is : ', count)
print('-' * 80)
#当前进程使用CPU的时间
ct = time.process_time()
print('CPU process time : ', ct)
print('-' * 80)
#将当前时间转换为指定格式的字符串
now_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒')
print('Now is : ', now_str)
print('-' * 80)
#将指定的时间转换为指定格式的字符串
time_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒',(2010,1,23,13,22,34,0,0,0))
print('Time is : ', time_str)
print('-' * 80)
#将指定时间字符串转换为struct_time对象
time_str = '2018-10-12'
st = time.strptime(time_str, '%Y-%m-%d')
print('Struct time is : ', st)
print('-' * 80)
#获取从1970年1月1日0点到现在过了多少秒
sds = time.time()
print('Seconds are : ', sds)
print('-' * 80)