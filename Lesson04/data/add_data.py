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
        #database='webprog'
    )
    # DBを操作するためのカーソルの作成  dictionary=True(フィールド名含む処理)
    cur = dbcon.cursor(dictionary=True)

except mydb.Error as e:
    #コネクション時にエラーが発生した場合，プログラム終了
    print(f"DBコネクションでエラー発生\n{e} ")
    sys.exit()

#もし，テーブルがすでにあれば削除
my_query( "DROP DATABASE IF EXISTS webprog;" )

#データベースの新規作成
my_query( "CREATE DATABASE webprog; ")
my_query( "USE webprog;" )
print("新規データベースwebprogを作成しました")

############# テーブルnaitei1の新規作成
sqlstring = """
    CREATE TABLE naitei1(
        naitei1_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        job VARCHAR(20),
        gender VARCHAR(20),
        club VARCHAR(20)
    )
"""
my_query( sqlstring )

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./naitei1.csv",header=0)
#weather.csvを1行ずつ処理
for ind,rowdata in df.iterrows():
    #data.Month は， data['Month'] とおなじ
    sqlstring = f"""
        INSERT INTO naitei1
        (job, gender, club)
        VALUES
        ('{rowdata.job}', '{rowdata.gender}' , '{rowdata.club}')
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring )   #1レコード挿入
    i += 1

print(f"naitei1 テーブル{i} レコード追加しました")

############# テーブルnaitei2の新規作成
sqlstring = """
    CREATE TABLE naitei2(
        naitei2_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        job VARCHAR(20),
        gender VARCHAR(20),
        club VARCHAR(20)
    )
"""
my_query( sqlstring )

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./naitei2.csv",header=0)
#weather.csvを1行ずつ処理
for ind,rowdata in df.iterrows():
    #data.Month は， data['Month'] とおなじ
    sqlstring = f"""
        INSERT INTO naitei2
        (job, gender, club)
        VALUES
        ('{rowdata.job}', '{rowdata.gender}' , '{rowdata.club}')
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring )   #1レコード挿入
    i += 1

print(f"naitei2 テーブル{i} レコード追加しました")

############# テーブルsiken1の新規作成
sqlstring = """
    CREATE TABLE siken1(
        siken1_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        cram VARCHAR(20),
        club VARCHAR(20),
        score int
    )
"""
my_query( sqlstring )

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./siken1.csv",header=0)
#weather.csvを1行ずつ処理
for ind,rowdata in df.iterrows():
    #data.Month は， data['Month'] とおなじ
    sqlstring = f"""
        INSERT INTO siken1
        (cram, club, score)
        VALUES
        ('{rowdata.cram}', '{rowdata.club}' , {rowdata.score})
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring )   #1レコード挿入
    i += 1

print(f"siken1 テーブル{i} レコード追加しました")

############# テーブルsiken2の新規作成
sqlstring = """
    CREATE TABLE siken2(
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
        INSERT INTO siken2
        (S_Number, Croom, Math, Eng, Jpn)
        VALUES
        ('{rowdata.S_Number}', '{rowdata.Croom}' , {rowdata.Math}, {rowdata.Eng}, {rowdata.Jpn})
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring )   #1レコード挿入
    i += 1

print(f"siken2 テーブル{i} レコード追加しました")

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
