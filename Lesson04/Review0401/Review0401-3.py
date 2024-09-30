#復習問題 0401　Flaskモジュールで，DBアクセス&データ分析
#このプログラムは，グラフファイルを出力するので，実行するディレクトリが重要
#Review0401.pyが存在するフォルダを，カレントディレクトリとして実行する

from flask import Flask,render_template
#Flaskのコンストラクタ
#プログラム中に作成するファイルを配置するフォルダ=static_folderは，imgフォルダとする
app = Flask(__name__ , static_folder="static")

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
    print(f"result1 \n{result1}")  #for debug
    result2 = siken.groupby("cram").std()
    print(f"result2 \n{result2}")  #for debug

    #テンプレートに引き渡すための文字列
    message = f"平均値 \n{result1['score']} \n"
    message += f"標準偏差 \n{result2['score']} \n"

    import matplotlib.pyplot as plt
    import japanize_matplotlib

    plt.bar(range(2),result1["score"],tick_label=["英語塾","行ってない"])
    plt.title("塾による平均値の違い")
    plt.xlabel("塾")
    plt.ylabel("試験結果")
    plt.savefig("./static/Review0401-2.png")
    plt.close()

    #render_templateにより，templateフォルダのindex.htmlを呼び出し
    return render_template("Review0401.html",
        title="cramの結果",
        message=message,
        image = "/static/Review0401-2.png"
    )

#塾cramごとの，平均値と標準偏差
@app.route("/club/")
def top3():
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
    #clubごとに分けて(groupby)して，平均値meanを計算
    #【入力】
    #print(f"result1 \n{result1}")  #for debug, output to terminal
    #【入力】
    #print(f"result2 \n{result2}")  #for debug, output to terminal



    #テンプレートに引き渡すための文字列
    #【入力】

    import matplotlib.pyplot as plt
    import japanize_matplotlib

    #【入力】
    plt.title("部活による平均値の違い")
    plt.xlabel("部活")
    plt.ylabel("試験結果")
    plt.savefig("【入力】")
    plt.close()

    #render_templateにより，templateフォルダのReview0401.htmlを呼び出し
    return render_template(
        #【入力】
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)

