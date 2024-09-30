#データベースを定義するプログラム

#questテーブルからレコードを検索するプログラム
import mysql.connector as mydb
import sys
import pandas as pd

def my_query(sqlstring , cur):#MYSQLにquery実行
    try:
        #クエリを実行する
        cur.execute( sqlstring )
    except mydb.Error as e:
        #クエリー実行にエラーが発生した場合，エラーメッセージとSQL文を表示しプログラム終了
        print("クエリ実行でエラー発生", e)
        print("sqlstring =",sqlstring)
        sys.exit()

def my_open( **dsn ):
#DBコネクションのインスタンス化
    try:
        #コネクションのインスタンス化
        dbcon = mydb.connect( **dsn )
        # DBを操作するためのカーソルの作成 dictionary=Trueは検索結果にフィールド名を含める場合
        cur = dbcon.cursor(dictionary=False)
    except mydb.Error as e:
        #コネクション時にエラーが発生した場合，プログラム終了
        print("DBコネクションでエラー発生", e)
        sys.exit()

    return dbcon , cur

def my_close(dbcon , cur ):
    cur.close()
    dbcon.close()

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbron03' #オープンするデータベース名

}

dbcon,cur = my_open( **dsn )

#データデースdbron03が無いときは新たに作成する
my_query("CREATE DATABASE IF not EXISTS dbron03;",cur)
#dbron03を指定する
my_query("USE dbron03;",cur)

#テーブルmeibo02を作成する。
my_query("DROP TABLE if EXISTS meibo03;",cur)
sqlstring = f"""
    CREATE TABLE meibo03(
        meibo03ID int not null auto_increment,
        namae varchar(30) not null,
        email varchar(50) not null,
        address varchar(50),
        primary key(meibo03ID)
    );
    
"""
my_query(sqlstring,cur)

#データベースのテーブル一覧
my_query("SHOW TABLES;",cur)

print("result: SHOW TABLES;")
for tbl in cur:
    print(tbl)

#テーブル構造の表示
my_query("DESC meibo03;",cur)
print("result: DESC meibo03;")
for col in cur:
    print(col)

#カーソルとDBコンソールのクローズ
my_close(dbcon,cur)
