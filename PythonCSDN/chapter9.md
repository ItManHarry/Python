# 数据分析

## Pygal

- Pygal下载安装

	使用：pip install pygal 安装即可
	
	安装完成后可通过：python -m pydoc -p 8899启动文档查看所有模块的信息

- 创建Pygal图

	1. 创建Pygal数据图对象，不同的数据图使用不同的类
	
	2. 调用数据图对象的add()方法添加数据
	
	3. 调用Congfig对象的属性配置数据图
	
		3.1. x_labels:X轴坐标
		
		3.2. title：标题
		
		3.3. x_title：X轴标题
		
		3.4. y_title：Y轴标题
	
	4. 调用数据图的render_to_xxx()方法将数据图渲染到指定的输出节点
	
```python
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
	python = [8.89, 9.23, 10.45, 11.25, 11.35, 11.23, 15.84,  17.12, 19.88]
	bar.add('Java', java)
	bar.add('C', c)
	bar.add('Python', python)
	bar.x_labels = years
	bar.x_title = 'Year'
	bar.y_title = 'Percent'
	#输出图片
	bar.render_to_file('languages.svg')
```	

- 水平柱状图

	类：pygal.HorizontalBar
	
	轴：x_labels配置Y轴刻度，y_labels配置X轴刻度
	
```python
	import pygal
	#创建对象
	bar = pygal.HorizontalBar()
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
	bar.y_title = 'Year'
	bar.x_title = 'Percent(%)'
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
	bar.render_to_file('languages4.svg')
```

- 折线图

```python
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
```

- 水平折线图

```python
	import pygal
	#创建对象
	bar = pygal.HorizontalLine()
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
	bar.y_title = 'Year'
	bar.x_title = 'Percent(%)'
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
	bar.render_to_file('languages5.svg')
```

- 叠加柱状图

```python
	import pygal
	#创建叠加柱状图
	bar = pygal.StackedBar()
	#设置标题
	bar.title = 'Fruit Sale Analysis'
	#添加数据
	years = [str(i) for i in range(2011, 2020)]
	print(years)
	banana = [17.89, 18.23, 20.45, 19.25, 20.35, 21.23, 19.84,  20.12, 19.88]
	apple = [12.89, 15.56, 16.45, 14.89, 13.98, 15.23, 14.89,  16.01, 15.98]
	orange = [8.89, 9.23, 10.45, 11.25, 11.35, 11.23, 15.84,  17.12, 20.11]
	bar.add('Banana', banana)
	bar.add('Apple', apple)
	bar.add('Orange', orange)
	bar.x_labels = years
	bar.y_title = 'Year'
	bar.x_title = 'Sale(KRMB)'
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
	bar.render_to_file('fruit.svg')
```

- 水平叠加柱状图

```python
	import pygal
	#创建水平叠加柱状图
	bar = pygal.HorizontalStackedBar()
	#设置标题
	bar.title = 'Fruit Sale Analysis'
	#添加数据
	years = [str(i) for i in range(2011, 2020)]
	print(years)
	banana = [17.89, 18.23, 20.45, 19.25, 20.35, 21.23, 19.84,  20.12, 19.88]
	apple = [12.89, 15.56, 16.45, 14.89, 13.98, 15.23, 14.89,  16.01, 15.98]
	orange = [8.89, 9.23, 10.45, 11.25, 11.35, 11.23, 15.84,  17.12, 20.11]
	bar.add('Banana', banana)
	bar.add('Apple', apple)
	bar.add('Orange', orange)
	bar.x_labels = years
	bar.y_title = 'Year'
	bar.x_title = 'Sale(KRMB)'
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
	bar.render_to_file('fruit3.svg')
```

- 叠加折线图

```python
	import pygal
	#创建叠加折线图
	bar = pygal.StackedLine()
	#设置标题
	bar.title = 'Fruit Sale Analysis'
	#添加数据
	years = [str(i) for i in range(2011, 2020)]
	print(years)
	banana = [17.89, 18.23, 20.45, 19.25, 20.35, 21.23, 19.84,  20.12, 19.88]
	apple = [12.89, 15.56, 16.45, 14.89, 13.98, 15.23, 14.89,  16.01, 15.98]
	orange = [8.89, 9.23, 10.45, 11.25, 11.35, 11.23, 15.84,  17.12, 20.11]
	bar.add('Banana', banana)
	bar.add('Apple', apple)
	bar.add('Orange', orange)
	bar.x_labels = years
	bar.y_title = 'Year'
	bar.x_title = 'Sale(KRMB)'
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
	bar.render_to_file('fruit2.svg')
```

- 水平叠加折线图

```python
	import pygal
	#创建水平叠加折线图
	bar = pygal.HorizontalStackedLine()
	#设置标题
	bar.title = 'Fruit Sale Analysis'
	#添加数据
	years = [str(i) for i in range(2011, 2020)]
	print(years)
	banana = [17.89, 18.23, 20.45, 19.25, 20.35, 21.23, 19.84,  20.12, 19.88]
	apple = [12.89, 15.56, 16.45, 14.89, 13.98, 15.23, 14.89,  16.01, 15.98]
	orange = [8.89, 9.23, 10.45, 11.25, 11.35, 11.23, 15.84,  17.12, 20.11]
	bar.add('Banana', banana)
	bar.add('Apple', apple)
	bar.add('Orange', orange)
	bar.x_labels = years
	bar.y_title = 'Year'
	bar.x_title = 'Sale(KRMB)'
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
	bar.render_to_file('fruit4.svg')
```

- 饼图

```python
	import pygal
	#数据
	data = {
		'Java':0.16881, 
		'c':0.14996, 
		'c++':0.07471,
		'python':0.06992,
		'vb.net':0.04762,
		'c#':0.03541,
		'PHP':0.02925,
		'JavaScript':0.02411,
		'SQL':0.02316,
		'Assembly':0.01409,
		'Other':0.36326
	}
	#创建饼图对象
	pie = pygal.Pie()
	for k,v in data.items():
		pie.add(k, v)
	pie.title = '2018 Programing Language'
	pie.legend_at_bottom = True
	pie.render_to_file('pie1.svg')
```

- 空心饼图

```python
	import pygal
	#数据
	data = {
		'Java':0.16881, 
		'c':0.14996, 
		'c++':0.07471,
		'python':0.06992,
		'vb.net':0.04762,
		'c#':0.03541,
		'PHP':0.02925,
		'JavaScript':0.02411,
		'SQL':0.02316,
		'Assembly':0.01409,
		'Other':0.36326
	}
	#创建饼图对象
	pie = pygal.Pie()
	for k,v in data.items():
		pie.add(k, v)
	pie.title = '2018 Programing Language'
	pie.legend_at_bottom = True
	#设置空心
	pie.inner_radius = 0.5
	pie.render_to_file('pie2.svg')
```

- 半圆饼图

```python
	import pygal
	#数据
	data = {
		'Java':0.16881, 
		'c':0.14996, 
		'c++':0.07471,
		'python':0.06992,
		'vb.net':0.04762,
		'c#':0.03541,
		'PHP':0.02925,
		'JavaScript':0.02411,
		'SQL':0.02316,
		'Assembly':0.01409,
		'Other':0.36326
	}
	#创建饼图对象
	pie = pygal.Pie()
	for k,v in data.items():
		pie.add(k, v)
	pie.title = '2018 Programing Language'
	pie.legend_at_bottom = True
	#设置空心
	pie.inner_radius = 0.5
	#设置为半圆
	pie.half_pie = True
	pie.render_to_file('pie3.svg')
```

- 点图

```python
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
```