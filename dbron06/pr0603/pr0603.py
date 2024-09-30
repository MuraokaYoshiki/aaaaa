# pr0603.py

from MyDatabase import my_open , my_query , my_close
import pandas as pd

#Data Source Nameのパラメータを辞書型変数で定義しオープン
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'pr0602' #オープンするデータベース名
}


from flask import Flask,render_template ,request
#Flaskのコンストラクタ
app = Flask(__name__ ,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    #DBオープン，SQLクエリの実行
    dbcon,cur = my_open( **dsn )
    sqlstring = f"""
        SELECT *
        FROM customer
        ;
    """
    my_query(sqlstring, cur)
    #結果を2元表で受け取り
    recset = pd.DataFrame( cur.fetchall())
    radio_data = pd.Series( recset["cname"])
    print(radio_data)

    return render_template( "pr0603-top.html",
        title = "文房具注文確認" ,
        radio_data = radio_data
    )

@app.route("/total1")
def total1():
    dbcon,cur = my_open( **dsn )

    sqlstring = f"""
        SELECT cname,sum(price) as  totalprice
        FROM item_cus_sal
        GROUP BY cname ;
    """
    my_query(sqlstring, cur)
    #結果を2元表で受け取り
    recset = pd.DataFrame( cur.fetchall())

    print( recset )

    #カーソルとDBコンソールのクローズ
    my_close(dbcon, cur)

    return render_template( "pr0603-table.html",
        title = f"文具注文の集計結果" ,
        table_data = recset
    )

@app.route("/detail1",methods = ["POST"])
def detail1():
    #フォーム変数の受け取り
    cname = request.form["cname"]

    #DBオープンとクエリ実行
    dbcon,cur = my_open( **dsn )
    sqlstring = f"""
        SELECT *
        FROM item_cus_sal
        WHERE cname = '{cname}' ;
    """
    my_query(sqlstring, cur)
    #結果を2元表で受け取り
    recset = pd.DataFrame( cur.fetchall())
    #customerIDフィールドを削除する
    table_data = recset.drop("customerID",axis=1)

    return render_template( "pr0603-table.html",
        title = f"{cname}の集計結果" ,
        table_data = table_data
    )


#プログラム起動
app.run(host="localhost",port=5000,debug=True)
