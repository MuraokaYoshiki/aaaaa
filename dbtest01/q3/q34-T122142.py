#q34-T122142.py
from MyDatabase import my_open , my_query , my_close
import pandas as pd

dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbtest01' #オープンするデータベース名
}

dbcon,cur = my_open( **dsn ) 
sqlstring = f"""
    SELECT * FROM ga_ka_at WHERE kamokucode='J002';
"""
my_query(sqlstring,cur) 
recset = pd.DataFrame(cur.fetchall())
#print(recset)確認用

my_close(dbcon, cur)

data = recset.loc[:,["gakusekicode", "namae", "classdate", "atdata"]]
#print(data)確認用
result = pd.pivot_table(data, index=["gakusekicode", "namae"], columns="classdate") 

result_out = result.applymap('{:,.0f}'.format)#小数点を消す

print(result_out)