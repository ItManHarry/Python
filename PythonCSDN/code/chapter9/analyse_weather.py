#获取天气数据
import urllib.request, re, datetime
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
def get_data(city, year, month):
    url = 'https://m.tianqi.com/lishi/%s/%s%s.html' %(city, year, month)
    print(url)
    req = urllib.request.Request(url=url, headers=headers)
    return urllib.request.urlopen(req).read().decode('UTF-8')
#print(get_data('yantai','2019','01'))
dates, highs, lows = [], [], []
city = 'yantai'
year ='2019'
monthes = ['%02d' %i for i in range(1, 13)]
print(monthes)
#定义一个开始日期，用于判断数据是否缺少某天
prev_day = datetime.datetime(2018, 12, 31)
for month in monthes:
    #下载网页源代码
    data = get_data(city, year, month)
    text = ''.join(data.split())
    #获取全部天气对应的正则表达式
    pattern = re.compile('<divclass="weatherbox">(.*?)</div><divclass="clearline1">')      
    div_list = pattern.findall(text)
    #获取每日天气
    pattern1 = re.compile('<dlclass="table_day15">(.*?)</dl>')
    if len(div_list) != 0:
        dls = pattern1.findall(div_list[0])
        print('dls length is : ', len(dls))
        for day in dls:
            #日期
            day_pattern = re.compile('<ddclass="date">(.*?)</dd>')
            data = day_pattern.findall(day)
            d_str = year + "/" + data[0][0:5]
            #温度
            temp_pattern = re.compile('<ddclass="txt2">(.*?)</dd>')
            data = temp_pattern.findall(day)
            #最低气温
            low_pattern = re.compile('^(.*?)~')
            low_temp = low_pattern.findall(data[0])[0]
            #最高气温
            high_pattern = re.compile('<b>(.*?)</b>')
            high_temp = high_pattern.findall(data[0])[0]
            #清洗数据
            try:
                cur_day = datetime.datetime.strptime(d_str, '%Y/%m/%d')
                low = int(low_temp)
                high = int(high_temp)
            except ValueError:
                print('Current day : ' , cur_day,  'temperature is wrong')
            else:
                #判断是否差某一天
                diff = cur_day - prev_day
                #如果两个日期的差值不是一天，说明丢失了数据
                if diff != datetime.timedelta(days = 1):
                    print('Before  lost data .')
                dates.append(d_str)
                lows.append(low)
                highs.append(high)
                prev_day = cur_day             
import pygal
#创建对象
line = pygal.Line()
#设置标题
line.title = 'Yantai Temperature(2019)'
#添加数据
line.add('Low', lows)
line.add('High', highs)
line.x_labels = dates
#显示X轴主刻度值
line.x_labels_major = dates[::30]
#不显示小刻度
line.show_minor_x_labels = False
line.x_label_rotation = 45
line.x_title = 'Date'
line.y_title = 'Temperature(℃)'
#输出图片
line.render_to_file('temperature.svg')                