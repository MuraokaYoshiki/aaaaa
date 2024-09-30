#q32-T122142.py 
# CSVファイルをテーブルにインポートするプログラム
import mysql.connector as mydb
import sys
import pandas as pd
from MyDatabase import my_query, my_open, my_close
import datetime

dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbtest01' #オープンするデータベース名
}

dbcon,cur = my_open( **dsn )

#データデースdbtest01が無いときは新たに作成する
my_query("CREATE DATABASE if not exists dbtest01;",cur)
#dbtest01を指定する
my_query("USE dbtest01;",cur)

#gakuseki
dt_now = datetime.datetime.now() # 現在の日時
i = 0 #レコード件数
filename = "./gakuseki.csv"
df = pd.read_csv(filename, header=0)
for ind,rowdata in df.iterrows():
    sqlstring = f"""
        INSERT INTO gakuseki(gakusekicode, namae, a_year, lastupdate)
        VALUES('{rowdata[0]}', '{rowdata[1]}', {rowdata[2]}, '{dt_now}');
    """
    my_query(sqlstring, cur)
    i += 1

print(f"{filename}を{i}レコードを新規挿入しました")

#kamoku
dt_now = datetime.datetime.now() # 現在の日時
i = 0 #レコード件数
filename = "./kamoku.csv"
df = pd.read_csv(filename, header=0)
for ind,rowdata in df.iterrows():
    sqlstring = f"""
        INSERT INTO kamoku(kamokucode, subjectname, tantou, lastupdate)
        VALUES('{rowdata[0]}', '{rowdata[1]}', '{rowdata[2]}', '{dt_now}');
    """
    my_query(sqlstring, cur)
    i += 1

print(f"{filename}を{i}レコードを新規挿入しました")

#attendance
dt_now = datetime.datetime.now() # 現在の日時
i = 0 #レコード件数
filename = "./attendance.csv"
df = pd.read_csv(filename, header=0)
for ind,rowdata in df.iterrows():
    sqlstring = f"""
        INSERT INTO attendance(gakusekicode, kamokucode, classdate, atdata, lastupdate)
        VALUES('{rowdata[0]}', '{rowdata[1]}', '{rowdata[2]}', '{rowdata[3]}', '{dt_now}');
    """
    my_query(sqlstring, cur)
    i += 1

print(f"{filename}を{i}レコードを新規挿入しました")

#デバック
sqlstring = f"""
    SELECT * FROM gakuseki;
"""
my_query(sqlstring, cur)
recset = pd.DataFrame(cur.fetchall())
#print(recset)確認用

sqlstring = f"""
    SELECT * FROM kamoku;
"""
my_query(sqlstring, cur)
recset = pd.DataFrame(cur.fetchall())
#print(recset)確認用

sqlstring = f"""
    SELECT * FROM attendance;
"""
my_query(sqlstring, cur)
recset = pd.DataFrame(cur.fetchall())
#print(recset)確認用

dbcon.commit()

my_close(dbcon,cur)
