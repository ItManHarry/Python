import pandas as pd
df = pd.read_csv('./DooQISData.csv',dtype=object)
#所有的数据
all = df.values
#print(type(all))
print(all[0:10])
with open('TempInsert.sql','wb') as f:
        for d in all[0:10]:          
            sql = "INSERT INTO DC_DOOQIS_CLAIMINFO (QMNUM , QSEQNO ,AUFNR  , ASEQNO  , CALMONTH_CMPL  , MATNR , EQUNR , TYPBZ , SERNR , QMDAB , WORKING_HR , ILART , RESP_LAST_DIV_1 , RESP_LAST_DIV_2 , WERKS , ZPP_PLANT , COMMENT1 , COMMENT2 , COMMENT3 , COMMENT4 , AEDAT) values ('"+str(d[0])+"','"+str(d[1])+"','"+str(d[2])+"',"+str(d[3])+","+str(d[4])+",'"+str(d[5])+"','"+str(d[6])+"','"+str(d[7])+"','"+str(d[8])+"','"+str(d[9])+"','"+str(d[10])+"','"+str(d[11])+"','"+str(d[12])+"','"+str(d[13])+"','"+str(d[14])+"','"+str(d[15])+"','"+str(d[16])+"','"+str(d[17])+"','"+str(d[18])+"','"+str(d[19])+"','"+str(d[20])+"');\r\n"
            f.write(sql.encode('utf-8')) 