from flask import Flask,render_template

#Flaskのコンストラクタ
app = Flask(__name__)

page_title = "郵便番号の検索をするページ"

#ルーティング定義
@app.route("/")
def top():
    return page_title

@app.route("/yuubin/茅野市")
def top2():
    page_title="茅野市郵便番号検索ページ"
    import pandas as pd
    from mydblib import my_select

    #post_areaのcityに対応するレコードを抽出する処理
    sqlstring = f"""
        SELECT *
        FROM post_area
        WHERE city ='茅野市'
        ;
    """
    qdata = my_select( sqlstring )
    #print( f"qdata\n{qdata}")  #for debug

    #print( f"cols {qdata.columns}")  #for debug 
    #print( f"data {qdata.values}")  #for debug

    return render_template("table.html",
        title = page_title,
        cols = qdata.columns,
        table_data = qdata.values
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)