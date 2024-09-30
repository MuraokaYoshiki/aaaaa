#mydblib.py　
#テーブルからレコードを抽出し，pandas DtaFrameに変換するモジュール
#制限事項：inner join など複数テーブルに対応していない
import mysql.connector as mydb
import sys
import pandas as pd

def my_select(sqlstring):

    # DBサーバにコネクションの作成
    # パラメータ host,port,user,password,database は，適宜変更する
    try:
        dbcon = mydb.connect(
            host='webprog_db',
            port='3306',
            user='dbuser',
            password='1234',
            database='sampledb'
        )
        # DBを操作するためのカーソルの作成  dictionary=True
        cur = dbcon.cursor(dictionary=True)

    except mydb.Error as e:
        #コネクション時にエラーが発生した場合，プログラム終了
        print(f"DBコネクションでエラー発生\n{e}")
        sys.exit()

    #クエリーの実行
    try:
        #クエリを実行し，結果をrecsetに代入する
        cur.execute( sqlstring )
        recset = cur.fetchall()
    except mydb.Error as e:
        #クエリー実行にエラーが発生した場合，プログラム終了
        print(f"クエリ実行でエラー発生\n{e}")
        print(f"入力されたSQLは\n{sqlstring}")
        sys.exit()
    
    return pd.DataFrame( recset )

