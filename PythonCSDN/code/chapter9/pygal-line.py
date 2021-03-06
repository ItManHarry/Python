import pygal
#创建对象
bar = pygal.Line()
#设置标题
bar.title = 'Program languages Percent'
#添加数据
years = [str(i) for i in range(2011, 2020)]
print(years)
java = [17.89, 18.23, 20.45, 19.25, 20.35, 21.23, 19.84,  20.12, 19.88]
c = [12.89, 15.56, 16.45, 14.89, 13.98, 15.23, 14.89,  16.01, 15.98]
python = [8.89, 9.23, 10.45, 11.25, 11.35, 11.23, 15.84,  17.12, 20.11]
bar.add('Java', java)
bar.add('C', c)
bar.add('Python', python)
bar.x_labels = years
bar.x_title = 'Year'
bar.y_title = 'Percent(%)'
#设置X轴标签选择度数
bar.x_label_rotation = -45
#设置图例放在下面
#bar.legend_at_bottom = True
#设置四周的页边距(也可单独设置：margin_bottom, margin_top, margin_left, margin_right)
bar.margin = 5
#显示Y轴的网格线
bar.show_y_guides = True
#显示X轴的网格线
bar.show_x_guides = True
#输出图片
bar.render_to_file('languages3.svg')