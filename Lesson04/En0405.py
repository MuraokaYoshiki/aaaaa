import numpy as np
from scipy import stats 
from mydblib2 import my_select
#SQL の設定
# table に検索する table 名

s  =0
i = 0
j = 0
sqlstring = f"""
    SELECT *
    FROM weather
    WHERE Area = 'Nagoya'
    ;
"""
#webprog データベースの weather テーブルのレコードを読み込み
weather = my_select( "webprog",sqlstring )
list = [0] * 12
for index in range(len(weather["Temp_mean"])):
    if(weather["Year"][s] <2010 or weather["Year"][s] >2019):
        s += 1
        continue
    if(i == 12):
        i = 0
    list[i] += weather["Temp_mean"][s]
    i += 1
    j += 1
    s += 1
t = (j + 1) / 12
list = [x / t for x in list]
a = list
#for j in list2:
    #print (round(j,3))
print("Nagoya:",round(np.mean(list),3))
Na = np.mean(list)


s  =0
i = 0
j = 0
sqlstring = f"""
    SELECT *
    FROM weather
    WHERE Area = 'Osaka'
    ;
"""
#webprog データベースの weather テーブルのレコードを読み込み
weather = my_select( "webprog",sqlstring )
list = [0] * 12
for index in range(len(weather["Temp_mean"])):
    if(weather["Year"][s] <2010 or weather["Year"][s] >2019):
        s += 1
        continue
    if(i == 12):
        i = 0
    list[i] += weather["Temp_mean"][s]
    i += 1
    j += 1
    s += 1
t = (j + 1) / 12
list = [x / t for x in list]
b = list
#for j in list2:
    #print (round(j,3))
print("Osaka:",round(np.mean(list),3))
Na = np.mean(list)


s  =0
i = 0
j = 0
sqlstring = f"""
    SELECT *
    FROM weather
    WHERE Area = 'Fukuoka'
    ;
"""
#webprog データベースの weather テーブルのレコードを読み込み
weather = my_select( "webprog",sqlstring )
list = [0] * 12
for index in range(len(weather["Temp_mean"])):
    if(weather["Year"][s] <2010 or weather["Year"][s] >2019):
        s += 1
        continue
    if(i == 12):
        i = 0
    list[i] += weather["Temp_mean"][s]
    i += 1
    j += 1
    s += 1
t = (j + 1) / 12
list = [x / t for x in list]
c = list
#for j in list2:
    #print (round(j,3))
print("Fukuoka:",round(np.mean(list),3))
Na = np.mean(list)

ans1,ans2 = stats.f_oneway(a,b,c)
ans3,ans4 = stats.ttest_ind(a,c)
ans5,ans6 = stats.ttest_ind(c,b)
print("一元配置分散分析：",round(ans2,3))



