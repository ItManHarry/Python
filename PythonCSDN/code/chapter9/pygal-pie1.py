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