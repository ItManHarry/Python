import pygal
import random
#数据
years = [str(i) for i in range(2011,2020)]
apple = [random.randint(15,25) * i for i in range(11,20)]
banana = [random.randint(10,20) * i for i in range(11,20)]
orange = [random.randint(10,20) * i for i in range(11,20)]
#点图对象
dot = pygal.Dot()
dot.add('Apple', apple)
dot.add('Banana', banana)
dot.add('Orange', orange)
#设置标题
dot.title = 'Fruit Sale Amount'
#设置X轴
dot.x_labels = years
dot.x_title = 'Year'
#显示Y轴的网格线
dot.show_y_guides = True
#显示X轴的网格线
dot.show_x_guides = True
dot.render_to_file('dot.svg')
