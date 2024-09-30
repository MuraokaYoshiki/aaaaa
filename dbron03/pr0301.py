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
        # DBを操作するためのカーソルの作成 dictionary=Trueは検索結果にフィールド名を含める場合 dictionary=Falseはフィールド名が0,1,..
        cur = dbcon.cursor(dictionary=True)
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
    'host' : 'webprog_db',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'sampledb' #オープンするデータベース名
}

#DBコネクションとカーソルを実体化
dbcon,cur = my_open(**dsn)

#sql文  f"""(ダブルコート3つ)は，複数行のf指定付きのSQL文を指定する
#SQLの中の文字列はシングルクォーテーションで囲む
sqlstring = f"""
	SELECT prefecture,COUNT(prefecture) AS prefcnt
    FROM quest
    GROUP BY prefecture
    ORDER BY prefcnt DESC
    ;
"""
#クエリ呼び出し
my_query(sqlstring,cur)

#クエリの結果を配列変数で読み込み
recset = pd.DataFrame(cur.fetchall())
print(recset)

#カーソルとDBコンソールのクローズ
my_close(dbcon,cur)