#fuku0501.py 
#FlaskモジュールでDBの操作
import re
from MyDatabase import my_open , my_query , my_close
import pandas as pd

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbron05' #オープンするデータベース名
}

from flask import Flask,render_template ,request
#Flaskのコンストラクタ
app = Flask(__name__ ,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    return render_template( "fuku0501-top.html",
        title = "Fuku0501トップ" 
    )

@app.route("/select")
def select():

    #DBオープン
    dbcon,cur = my_open(**dsn)
    
    #すべてのデータ検索のためのSQL文
    sqlstring = f"""
        SELECT *
        FROM meibo
        ;
    """
    my_query(sqlstring,cur)
    recset = pd.DataFrame(cur.fetchall())

    return render_template("fuku0501-table.html",
        title = "Fuku0501トップ" ,
        table_data = recset
    )

@app.route("/insert1")
def insert1():
    return render_template("fuku0501-form.html",
        title="新規レコード挿入"
    )

@app.route("/insert2",methods=["POST"])
def insert2():
    #DBオープン
    dbcon,cur = my_open(**dsn)
    
    #データ挿入のためのSQL文
    sqlstring = f"""
        INSERT INTO meibo
        (gakuseki,namae,yomi,acyear,math,eng)
        VALUES
        ('{request.form["gakuseki"]}',
        '{request.form["namae"]}',
        '{request.form["yomi"]}',
        {request.form["acyear"]},
        {request.form["math"]},
        {request.form["eng"]}
        )
        ;
    """
    my_query(sqlstring,cur)
    dbcon.commit()
    my_close(dbcon,cur)

    return render_template( "fuku0501-msg.html",
        title="レコード挿入完了",
        msg = "レコード挿入しました"
    )

@app.route("/analysis1")
def analysis1():
    #DBオープン
    dbcon,cur = my_open(**dsn)
    
    sqlstring = """
        SELECT *
        FROM meibo
        ;
    """
    my_query( sqlstring,cur)
    recset = pd.DataFrame( cur.fetchall())
    #数学と英語の列のみ抽出
    dataset = recset.loc[:,["math","eng"]]
    #print(dataset) #for debug
    #要約統計量の計算
    result = dataset.describe()

    my_close(dbcon,cur)

    return render_template("fuku0501-msg.html",
        title = "要約統計量",
        message = result
    )

@app.route("/analysis2")
def analysis2():
    from scipy import stats
    #DBオープン
    dbcon,cur = my_open(**dsn)
    
    sqlstring = """
        SELECT *
        FROM meibo
        ;
    """
    my_query( sqlstring,cur)
    recset = pd.DataFrame( cur.fetchall())
    #数学と英語の列のみ抽出
    math =  recset["math"]
    eng = recset["eng"]
    #t検定
    t_value, p_value = stats.ttest_ind(math,eng)

    msg = f"平均値　数学={math.mean():.3f}  英語={eng.mean():.3f} \n"
    msg += f"統計量　t値={t_value:.3f}  p値={p_value:.3f}"
    if p_value < 0.05 :
        msg += "　平均値に有意差あり"
    else:
        msg += "　平均値に有意差なし"

    my_close(dbcon,cur)

    return render_template( "fuku0501-msg.html",
        message = msg
    )
"""

#プログラム起動
app.run(host="localhost",port=5000,debug=True)
