# 演習2　勤怠管理DBの社員テーブルと所属部署テーブルを連結し，女性社員のレコードのみ抽出する
#すべての列を表示する。
#
import mysql.connector as mydb
import sys
import pandas as pd

# DBサーバにコネクションの作成
try:
    dbcon = mydb.connect(
        host='webprog_db',
        port='3306',
        user='dbuser',
        password='1234',
        database='sampledb'
    )
   # DBを操作するためのカーソルの作成 連想配列を指定
    cur = dbcon.cursor(dictionary=True)
except mydb.Error as e:
    #コネクション時にエラーが発生した場合，プログラム終了
    print("DBコネクションでエラー発生", e)
    sys.exit()

# コネクションが切れた時に再接続してくれるよう設定
#conn.ping(reconnect=True)

#クエリーの実行 社員テーブルをdf_employee(pandas DF)に代入する
try:
    cur.execute( 
        """
        SELECT *
        FROM kinmu_employee
        INNER JOIN kinmu_depart
        on kinmu_employee.depart_id = kinmu_depart.depart_id
        WHERE gender = 2
        ;
        """
    )
    #クエリ実行結果を recsetに代入する
    recset = cur.fetchall()
    df_employee = pd.DataFrame( recset )
except mydb.Error as e:
    #クエリー実行にエラーが発生した場合，プログラム終了
    print("クエリ実行でエラー発生", e)
    sys.exit()

#結果の一括(list型)表示
print( "recset = ",recset)

#結果を1行ずつ(dict型)表示
for rowdata in recset:
    print( rowdata )

#3行目のデータを表示
print( "2行目のデータ:",recset[2])

#3行目のl_nameを表示
print( "3行目のl_nameを表示",recset[1]["l_name"])
