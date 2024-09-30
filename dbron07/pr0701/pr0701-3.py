#pr0701-2.py student.csvをDBにインポートするプログラム
import pandas as pd
import re
from ssl import MemoryBIO
from MyDatabase import my_open , my_query , my_close
import pandas as pd
from flask import Flask,render_template ,request
from werkzeug.datastructures import FileStorage
import chardet

#Flask のコンストラクタ
app = Flask(__name__ ,static_folder="static")
#ファイル最大サイズを 16MByte に設定
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbron07' #オープンするデータベース名
}

dbcon,cur = my_open( **dsn )

@app.route("/")
def top():
    return render_template( "pr0701-top_form.html",
        title = "出席CSVアップロード画面" 
    )

from werkzeug.datastructures import FileStorage
import chardet

#2つのファイルを処理するための繰り返し処理 fnにファイル名が入る

@app.route("/upload_csv", methods=["POST"])
def uplaod_csv():
    #csv ファイルの受け取り
    csv_data = request.files["upfile"]
    # print( csv_data ) #for debug
    #CSV データを DataFrame として読み込み
    df = pd.read_csv(csv_data) 
    print(df) #for debug

    dbcon,cur = my_open( **dsn )

    #2つのファイル名をlist変数として保存
    filename = ["./sekidata01.csv","./sekidata02.csv","./sekidata03.csv"]

    #現在の日時を取得
    import datetime
    dt_now = datetime.datetime.now()

    #2つのファイルを処理するための繰り返し処理 fnにファイル名が入る
    for fn in filename:

        #ファイルオープン 先頭行をheaderとして
        df = pd.read_csv(fn,header=0)

        #recsetは，DataFrameのため，indexとrowdataをペアで取得する
        for ind,rowdata in df.iterrows():

            #レコードを挿入するSQL文をそれぞれ定義する
            sqlstring = f"""
                INSERT INTO seki
                (s_code , jcnt , sekidata, lastupdate)
                values
                ('{rowdata[0]}',{rowdata[1]},{rowdata[2]},'{dt_now}')
                ;
            """
            #クエリー実行
            my_query(sqlstring, cur)

        #INSERT文を実行するループが終了し，結果をフィードバック
        print( f"{fn}を{len( df )}レコードを新規挿入しました")

        #テーブルに書き込み
        dbcon.commit()
        
    return render_template("pr0701-table.html",
    title = f"{df.shape[0]}レコードを新規挿入しました",
    filename = f"アップされたファイル名 {csv_data.filename}",
    table_data = df
    )

@app.route("/kakunin")
def kakunin():
    #dbオープン
    dbcon,cur = my_open( **dsn )
    #SQLの設定と，クエリ実行
    sqlstring = f"""
        SELECT *
        FROM std_seki
        ;
    """
    #クエリー実行
    my_query(sqlstring, cur)
    recset = pd.DataFrame(cur.fetchall())
    #print(recset.shape) #for debug


        #pivotテーブルで学生×科目の2元表
    data = recset.loc[:,["s_code","namae","jcnt","sekidata"]]
    result = pd.pivot_table(data , index=["s_code","namae"],columns="jcnt")


    #カーソルと DB コンソールのクローズ
    my_close(dbcon, cur) 

    return render_template("pr0701-msg.html",
        title = "出席の集計結果",
        message = result
    )


#プログラム起動
app.run(host="localhost",port=5000,debug=True) 