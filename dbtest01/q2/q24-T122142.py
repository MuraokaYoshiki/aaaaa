#q24-T122142.py 
#FlaskモジュールでDBの操作

from MyDatabase import my_open , my_query , my_close
import pandas as pd
import numpy as np

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbtest01' #オープンするデータベース名
}

from flask import Flask,render_template ,request
#Flaskのコンストラクタ
app = Flask(__name__ ,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    return render_template( "top.html",
        title = "売り上げ管理DB" 
    )

@app.route("/select_all")
def select_all():
    dbcon,cur = my_open( **dsn )
    sqlstring = f"""
        SELECT *
        FROM uriage
        ORDER BY s_date ASC
        ;
    """
    my_query(sqlstring,cur)
    recset = pd.DataFrame(cur.fetchall())
    
    my_close(dbcon,cur)
    
    return render_template( "select_all.html",
        title = "全てのレコード一覧表示" , 
        table_data = recset
    )

@app.route("/tantou1")
def tantou1():
    dbcon,cur = my_open( **dsn ) 
    
    sqlstring = f"""
        SELECT DISTINCT tantou
        FROM uriage
        ;
    """
    my_query(sqlstring,cur) 
    recset = pd.DataFrame(cur.fetchall())
    print(recset.shape) #for debug

    my_close(dbcon, cur) 
    return render_template( "tantou1.html", 
    title = "担当者選択画面", 
    select_data = recset 
    )

@app.route("/tantou2", methods=["POST"])
def tantou2():
    tantou = request.form["tantou"]
    dbcon,cur = my_open( **dsn ) 
    
    sqlstring = f"""
        SELECT *
        FROM uriage
        WHERE cancelflag = False AND tantou = '{tantou}'
        ORDER BY s_date ASC
        ;
    """
    my_query(sqlstring,cur) 
    recset = pd.DataFrame(cur.fetchall())
    
    my_close(dbcon, cur) 
    return render_template( "tantou2.html", 
        title = f"担当者{tantou}の打ち上げ一覧", 
        table_data = recset 
    ) 

@app.route("/cancel1_select")
def cancel1_select():
    dbcon,cur = my_open( **dsn ) 
    
    sqlstring = f"""
        SELECT *
        FROM uriage
        ORDER BY s_date ASC
        ;
    """
    my_query(sqlstring,cur) 
    recset = pd.DataFrame(cur.fetchall())

    my_close(dbcon,cur) 
    return render_template( "cancel1_select.html", 
        title="キャンセルレコード選択画面", 
        table_data = recset
    )

@app.route("/cancel2_select", methods=["POST"])
def cancel2_select():
    uriageID = request.form["uriageID"]
    dbcon,cur = my_open( **dsn ) 
    sqlstring = f"""
        SELECT *
        FROM uriage
        WHERE uriageID = {uriageID}
        ;
    """
    my_query(sqlstring,cur) 
    recset = pd.DataFrame(cur.fetchall())
    result = {"担当者":recset.tantou[0], "地域":recset.area[0], "売上額":recset.sales[0], "売り上げ日":recset.s_date[0]}

    my_close(dbcon,cur) 
    return render_template( "cancel2_select.html", 
        title = f"uriageID{uriageID}のキャンセル画面", 
        table_data = result, 
        uriageID = uriageID
    )
    
@app.route("/cancel3_select", methods=["POST", "GET"])
def cancel3_select():
    uriageID = request.args.get('uriageID', '')
    dbcon,cur = my_open( **dsn ) 
    sqlstring = f"""
        UPDATE uriage
        SET cancelflag = True
        WHERE uriageID = {uriageID}
        ;
    """
    my_query(sqlstring,cur)
    
    dbcon.commit()  
    my_close(dbcon,cur) 
    return render_template( "cancel3_select.html", 
        title = "レコードを削除",   
        message = f"UriageID{uriageID}のレコードを削除しました"
    )

@app.route("/pivot")
def pivot():
    dbcon,cur = my_open( **dsn ) 
    sqlstring = f"""
        SELECT tantou, area, SUM(sales)
        FROM uriage
        GROUP BY tantou, area
        ;
    """
    my_query(sqlstring,cur) 
    recset = pd.DataFrame(cur.fetchall())
    my_close(dbcon, cur)

    data = recset
    result = pd.pivot_table(data, index="tantou", columns="area", margins=True, aggfunc=np.sum)
    
    result_out = result.applymap('{:,.1f}'.format)

    print(result_out) #for debug
    #print(f"result.index : {result.index}") #for debug
    #print(f"result.columns : {result.columns}") #for debug
    #print(f"result.values : {result.values}") #for debug
    
    return render_template( "pivot.html", 
        title = "担当者×地域の集計結果",
        table_data = result_out
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)
