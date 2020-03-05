import pygal
#创建对象
bar = pygal.Bar()
#设置标题
bar.title = 'Program languages Percent'
#添加数据
years = [str(i) for i in range(2011, 2020)]
print(years)
java = [17.89, 18.23, 20.45, 19.25, 20.35, 21.23, 19.84,  20.12, 19.88]
c = [12.89, 15.56, 16.45, 14.89, 13.98, 15.23, 14.89,  16.01, 15.98]
python = [8.89, 9.23, 10.45, 11.25, 11.35, 11.23, 15.84,  17.12, 20.21]
bar.add('Java', java)
bar.add('C', c)
bar.add('Python', python)
bar.x_labels = years
bar.x_title = 'Year'
bar.y_title = 'Percent(%)'
#输出图片
bar.render_to_file('languages1.svg')