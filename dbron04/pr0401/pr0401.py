#pr0401　Flaskモジュールで，DBアクセス&データ分析
from MyDatabase import my_open , my_query , my_close
import pandas as pd

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'sampledb' #オープンするデータベース名
}

#flaskモジュールのインポートと実体化　<== お決まり
from flask import Flask, render_template , request
app = Flask(__name__ ,static_folder="static")

#---------------------------------------
#ルーティング定義
@app.route("/")
def top():
    return render_template( "pr0401-top.html",
        title = "アンケート回答者の都道府県名"      
    )

#地点と年度を選択するフォーム
@app.route("/search",methods=["POST"])
def search():
    #Data Source Nameのパラメータを辞書型変数で定義
    dsn = {
        'host' : '172.30.0.10',  #ホスト名(IPアドレス)
        'port' : '3306',        #mysqlの接続ポート番号
        'user' : 'root',      #dbアクセスするためのユーザid
        'password' : '1234',    #ユーザidに対応するパスワード
        'database' : 'sampledb' #オープンするデータベース名
    }
    dbcon,cur = my_open( **dsn )

    #フォーム変数を受け取る
    prefecture = request.form["prefecture"]
    
    #都道府県名と都市名で郵便番号を抽出するSQL
    sqlstring = f"""
		SELECT *
        FROM quest
        WHERE prefecture = '{prefecture}'
        ORDER BY prefecture
        ;
    """
    #query実行
    my_query( sqlstring , cur)
    recset = pd.DataFrame( cur.fetchall() )
    #print( recset )

    #dbのクローズ
    my_close( dbcon , cur  )

    return render_template(  "pr0401-table.html",
        title=f"{prefecture}のレコード一覧",
        table_data = recset
    )

#----------------------------------------------

#プログラム起動
app.run(host="localhost",port=5000,debug=True)
