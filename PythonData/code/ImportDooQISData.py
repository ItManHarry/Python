import pandas as pd
#安装原格式读取数据，dtype设置为object
#如:'000302860705',如果不指定dtype=object,读取后为'302860705',设置后便可正常读取
df = pd.read_csv('./DooQISData.csv',dtype=object,encoding='gbk')
#所有的数据
all = df.values
#print(type(all))
print(all[0:1])
#记录总数
total = len(df.values)
#每份条数
limit = 100000
#print(total // limit)  整除
#print(total % limit)  取余
print('-' * 100)
#余数是否为零
left = total % limit
#计算记录份数
parts = total // limit if not left else  total // limit + 1
#print('Parts size is : ', parts)
print('-' * 100)
#记录起始index
start = 0
#记录终止index
end = 0
#执行生成SQL文件
for part in range(parts):   
    start =  part * limit
    if part == parts -1:
        print('Last part !!!')
        end = start + (1 if not left else left)
    else:
        print('Normal part !!!')
        end = (part + 1) * limit
    print('From : ', start, ', to : ', end)
    file = 'InsertData'+str(part)+'.sql'
    print('Generate SQL file, file name :  ', file)
    #写入文件
    #计数器
    count = 0
    with open(file,'wb') as f:
        for d in all[start:end]:    
            count += 1
            print('正在执行写入第('+str(count)+')行SQL语句......',)
            sql = "INSERT INTO DC_DOOQIS_CLAIMINFO (QMNUM , QSEQNO ,AUFNR  , ASEQNO  , CALMONTH_CMPL  , MATNR , EQUNR , TYPBZ , SERNR , QMDAB , WORKING_HR , ILART , RESP_LAST_DIV_1 , RESP_LAST_DIV_2 , WERKS , ZPP_PLANT , COMMENT1 , COMMENT2 , COMMENT3 , COMMENT4 , AEDAT) values ('"+str(d[0])+"','"+str(d[1])+"','"+str(d[2])+"',"+str(d[3])+","+str(d[4])+",'"+str(d[5])+"','"+str(d[6])+"','"+str(d[7])+"','"+str(d[8])+"','"+str(d[9])+"','"+str(d[10])+"','"+str(d[11])+"','"+str(d[12])+"','"+str(d[13])+"','"+str(d[14])+"','"+str(d[15])+"','"+str(d[16])+"','"+str(d[17])+"','"+str(d[18])+"','"+str(d[19])+"','"+str(d[20])+"');\r\n"
            f.write(sql.encode('utf-8')) 
    print('SQL脚本文件(',file,')生成完毕......')
print('所有SQL脚本生成完毕......')    