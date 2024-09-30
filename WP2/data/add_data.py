import mysql.connector as mydb
import sys
import pandas as pd

#クエリーの実行
def my_query( sqlstring ):
    try:
        #クエリを実行し，結果をrecsetに代入する
        cur.execute( sqlstring )
    except mydb.Error as e:
        #クエリー実行にエラーが発生した場合，プログラム終了
        print(f"クエリ実行でエラー発生\n{e}")
        print(f"入力されたSQL文は\n{sqlstring}")
        sys.exit()


########### mainルーチン ############

#webprogDBコネクション
try:
    dbcon = mydb.connect(
        host='webprog_db',
        port='3306',
        user='root',
        password='1234'
        #database='wptest'
    )
    # DBを操作するためのカーソルの作成  dictionary=True(フィールド名含む処理)
    cur = dbcon.cursor(dictionary=True)

except mydb.Error as e:
    #コネクション時にエラーが発生した場合，プログラム終了
    print(f"DBコネクションでエラー発生\n{e} ")
    sys.exit()

db="wptest"
#もし，テーブルがすでにあれば削除
my_query( f"DROP DATABASE IF EXISTS {db};" )

#データベースの新規作成
my_query( f"CREATE DATABASE {db}; ")
my_query( f"USE {db};" )
print(f"新規データベース{db}を作成しました")

############# テーブルirisの新規作成
sqlstring = """
    CREATE TABLE iris(
        iris_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        sepallength FLOAT,
        sepalwidth FLOAT,
        petallength FLOAT,
        petalwidth FLOAT,
        kinds VARCHAR(20)
    )
"""
my_query( sqlstring )

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./iris.csv",header=0)
#weather.csvを1行ずつ処理
for ind,rowdata in df.iterrows():
    #data.Month は， data['Month'] とおなじ
    sqlstring = f"""
        INSERT INTO iris
        (sepallength, sepalwidth, petallength,petalwidth,kinds)
        VALUES
        ({rowdata.sepallength}, {rowdata.sepalwidth} , {rowdata.petallength}, {rowdata.sepalwidth}, '{rowdata.kinds}')
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring )   #1レコード挿入
    i += 1

print(f"iris テーブル{i} レコード追加しました")

############# テーブルsikenの新規作成
sqlstring = """
    CREATE TABLE siken(
        siken2_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        S_Number VARCHAR(20),
        Croom VARCHAR(20),
        Math int,
        Eng int,
        Jpn int
    )
"""
my_query( sqlstring )

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./siken2.csv",header=0)
#weather.csvを1行ずつ処理
for ind,rowdata in df.iterrows():
    #data.Month は， data['Month'] とおなじ
    sqlstring = f"""
        INSERT INTO siken
        (S_Number, Croom, Math, Eng, Jpn)
        VALUES
        ('{rowdata.S_Number}', '{rowdata.Croom}' , {rowdata.Math}, {rowdata.Eng}, {rowdata.Jpn})
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring )   #1レコード挿入
    i += 1

print(f"siken テーブル{i} レコード追加しました")

############# テーブルweatherの新規作成
sqlstring = """
    CREATE TABLE weather(
        Weather_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Month INT ,
        Year INT,
        Area VARCHAR(20),
        Temp_max float,
        Temp_mean float,
        Temp_min float,
        Precipitation float,
        Sunshine float
    )
"""
my_query( sqlstring )

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./weather.csv",header=0)
#weather.csvを1行ずつ処理
for ind,rowdata in df.iterrows():
    #data.Month は， data['Month'] とおなじ
    sqlstring = f"""
        INSERT INTO weather
        (month,year,area,temp_max,temp_mean,temp_min,precipitation,sunshine)
        VALUES
        ({rowdata.Month}, {rowdata.Year} , '{rowdata.Area}' , {rowdata.Temp_max} , {rowdata.Temp_mean} , 
        {rowdata.Temp_min} , {rowdata.Precipitation} , {rowdata.Sunshine} )
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring )   #1レコード挿入
    i += 1

print(f"weatherテーブル {i} レコード追加しました")

#DBに書き込み
dbcon.commit()  

#カーソルとDBコンソールのクローズ
cur.close()
dbcon.close()
