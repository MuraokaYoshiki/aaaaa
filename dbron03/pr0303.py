#questテーブルからレコードを検索するプログラム
from MyDatabase import my_open , my_query , my_close

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbron03' #オープンするデータベース名
}

dbcon,cur = my_open( **dsn )


#現在の日時を取得
import datetime
dt_now = datetime.datetime.now()

import pandas as pd

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./seiseki01.csv",header = 0)

#dbron03を指定する
my_query("USE dbron03;",cur)

#テーブルseisekiを作成する。
my_query("DROP TABLE if exists seiseki;",cur)

sqlstring = f"""
    CREATE TABLE seiseki(
        gakuseki varchar(5) not null,
        namae varchar(20),
        gpa  float,
        gps  float
    );
"""
my_query(sqlstring,cur)
dbcon.commit() 

sqlstring = f"""
    ALTER TABLE seiseki
        ADD COLUMN seisekiID INT AUTO_INCREMENT,
        ADD COLUMN lastupdate datetime,
        ADD PRIMARY KEY(seisekiID);
"""
my_query(sqlstring,cur)

#テーブルに書き込み
dbcon.commit() 

for ind,rowdata in df.iterrows():
    
    sqlstring = f"""
        INSERT INTO seiseki
        (gakuseki, namae, gpa, gps,  lastupdate)
        VALUES
        ('{rowdata.gakuseki}','{rowdata.namae}',{rowdata.gpa},{rowdata.gps},'{dt_now}' )
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring ,cur)   #1レコード挿入
    i += 1

print(f"seisekiテーブル{i} レコード追加しました")

#テーブルに書き込み
dbcon.commit() 

#カーソルとDBコンソールのクローズ
my_close(dbcon , cur)

