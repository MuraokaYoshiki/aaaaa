#例題4　SELECTの例(cursorの作成時 dictonary=True)

import mysql.connector as mydb
import sys

# DBサーバにコネクションの作成
try:
    dbcon = mydb.connect(
        host='webprog_db',
        port='3306',
        user='dbuser',
        password='1234',
        database='sampledb'
    )
    # DBを操作するためのカーソルの作成  dictionary=True(フィールド名含む処理)
    cur = dbcon.cursor(dictionary=True)

except mydb.Error as e:
    #コネクション時にエラーが発生した場合，プログラム終了
    print(f"DBコネクションでエラー発生\n{e} ")
    sys.exit()

#処理時間が多く要するなどの理由でコネクションが切れた時，再接続する設定
#conn.ping(reconnect=True)

#SQLの設定
sqlstring = """
        SELECT *
        FROM postarea
        WHERE city = '茅野市'
        ;
        """

#クエリーの実行
try:
    #クエリを実行し，結果をrecsetに代入する
    cur.execute( sqlstring )
    recset = cur.fetchall()
except mydb.Error as e:
    #クエリー実行にエラーが発生した場合，プログラム終了
    print(f"クエリ実行でエラー発生\n{e}")
    print(f"入力されたSQL文は\n{sqlstring}")
    sys.exit()

#for debug
print("recsetは，dict型のリスト")
print( f"recset=\n{recset}")

#リスト型のrecsetをpandas DataFrameに変換し保存する
import pandas as pd
post_number = pd.DataFrame(recset)
print(f"DBの検索結果\n{post_number}")