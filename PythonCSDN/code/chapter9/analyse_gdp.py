import urllib.request
import re
import json
with open('gdp.json', 'r',1,'utf-8') as f:
    #print(f.read())
    datas =  json.loads(f.read())
print('-' * 80)    
print(type(datas))
#print(datas[0])
countries = ['中国','美国','英国','法国','德国']
#GPD
gdps = [{},{},{},{},{}]
for data in datas:
    for  i, name in enumerate(countries):
        if data['CountryName'] == name:
            year = data['Year']
            gdps[i][year] = data['Value']
#print('GDP data is : ', gdps)  
#Get years
years = [] 
for key in gdps[0].keys():
    years.append(key)
print('-' * 80)
#年度排序
years.sort()
print('Years : ', years)
print('-' * 80)
gdp_list = [[],[],[],[],[]]    
for i in range(len(gdp_list)):
    print('Index is : ', i)
    for year in years:
        print('Year is : ', year)
        #除以10的9次方(十亿)
        gdp_list[i].append(gdps[i][year] / 1e9)
    print('-' * 80)
print('GPD List Is : ', gdp_list)  
#Create bar
import pygal
bar = pygal.Bar()
bar.title = 'Country GDP'
for i, country in enumerate(countries):
    bar.add(country, gdp_list[i])
bar.x_labels = years
bar.x_title = 'Year'
bar.y_title = 'GDP(Billion)'
bar.x_label_rotation = 45
bar.show_y_guides = True
bar.show_x_guides = False
bar.render_to_file('gdp.svg')    