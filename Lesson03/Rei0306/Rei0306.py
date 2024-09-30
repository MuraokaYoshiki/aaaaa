from flask import Flask,render_template

#Flaskのコンストラクタ
app = Flask(__name__)

page_title = "事業所別郵便番号の件数を検索するページ"

#ルーティング定義
@app.route("/")
def top():
    return page_title

@app.route("/samp/")
def top2():
    import pandas as pd
    from mydblib import my_select

    #post_areaのcityに対応するレコードを抽出する処理
    sqlstring = f"""
        SELECT city,count(postnumber) as pcnt
        FROM post_office
        WHERE city IN ('茅野市','長野市','松本市')
        GROUP BY city
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