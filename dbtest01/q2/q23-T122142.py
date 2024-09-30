#q23-T122142.sql  CSVファイルをテーブルにインポートするプログラム

#questテーブルからレコードを検索するプログラム
from MyDatabase import my_open , my_query , my_close

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbtest01' #オープンするデータベース名
}

dbcon,cur = my_open( **dsn )


#現在の日時を取得
import datetime
dt_now = datetime.datetime.now()

import pandas as pd

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./uriage.csv",header=0)
#weather.csvを1行ずつ処理
for ind,rowdata in df.iterrows():
    
    sqlstring = f"""
        INSERT INTO uriage
        (tantou,area,sales,s_date,lastupdate)
        VALUES
        ('{rowdata[0]}','{rowdata[1]}',{rowdata[2]},'{rowdata[3]}','{dt_now}')
    """
    #print( sqlstring )  #for debug
    my_query(sqlstring ,cur)   #1レコード挿入
    i += 1

print(f"./uriage.csvを{i}レコードを新規挿入しました")

#テーブルに書き込み
dbcon.commit() 

#カーソルとDBコンソールのクローズ
my_close(dbcon , cur)