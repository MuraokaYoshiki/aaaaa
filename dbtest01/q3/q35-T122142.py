#q35-T122142.py

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
    SELECT kamokucode, subjectname, SUM(atdata) AS cnt
    FROM ga_ka_at
    WHERE gakusekicode='H1004'
    GROUP BY kamokucode
    ;
"""
my_query(sqlstring,cur) 
recset = pd.DataFrame(cur.fetchall())
print(recset)
my_close(dbcon, cur)