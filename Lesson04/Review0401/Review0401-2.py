#復習問題 0401-2　Flaskモジュールで，DBアクセス&データ分析
#このプログラムは，グラフファイルを出力するので，実行するディレクトリが重要
#Review0401.pyが存在するフォルダを，カレントディレクトリとして実行する

from flask import Flask,render_template
#Flaskのコンストラクタ
#プログラム中に作成するファイルを配置するフォルダ=static_folder
app = Flask(__name__ , static_folder="【入力】")

#ルーティング定義
@app.route("/")
def top():
    return render_template( "Review0401.html",
        title = "復習問題01",
        message = "FlaskでDBアクセス&データ分析",
        image = ""
    ) 

#塾cramごとの，平均値と標準偏差
@app.route("/cram/")
def top2():
    #例題XXX　t検定
    import pandas as pd
    #データベースを引数で指定できるバージョン
    from mydblib2 import my_select

    #SQLの設定 
    # tableに検索するtable名 
    sqlstring =  f"""
        SELECT *
        FROM siken1
        ;
    """
    #webprogデータベースのsiken1テーブルのレコードを読み込み
    siken = my_select( "webprog",sqlstring )
    #cram英語塾に行っている人と行っていない人に分けて(groupby)して，平均値meanを計算
    result1 = siken.groupby("cram").mean()
    #print(f"result1 \n{result1}")  #for debug, output to terminal
    result2 = siken.groupby("cram").std()
    #print(f"result2 \n{result2}")  #for debug, output to terminal

    #テンプレートReview0401.html に受け渡すための文字列
    msg = f"平均値 \n{result1['score']} \n"
    msg += f"標準偏差 \n{result2['score']} \n"

    import matplotlib.pyplot as plt
    import japanize_matplotlib

    #棒グラフ表示
    #【入力】
    plt.title("塾による平均値の違い")
    plt.xlabel("塾")
    plt.ylabel("試験結果")
    #plt.savefig("【入力】")
    plt.close()

    #render_templateにより，templateフォルダのindex.htmlを呼び出し
    return render_template("Review0401.html",
        title="t検定の結果",
        message = msg,
        #image = 【入力】
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)

