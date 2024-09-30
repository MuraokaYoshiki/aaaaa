#En0401　Flaskモジュールで，DBアクセス&データ分析
#このプログラムは，グラフファイルを出力するので，実行するディレクトリが重要
#En0401.pyが存在するディレクトリを，カレントディレクトリとして実行する

from flask import Flask,render_template #【入力】
#Flaskのコンストラクタ
app = Flask(__name__ ,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    return render_template( "Rei0403.html",
        title = "各地の年間平均気温",
        message = "各地の平均気温を表示するには，http://localhost:5000/form "
    ) 

#地点と年度を選択するフォーム
@app.route("/form")
def top2():
    return render_template( 
        "form.html",
        title="地域，年度選択フォーム"
    )

#地点と年度を選択するフォーム
@app.route("/search",【入力】)
def top3():
    #form変数を受け取り
    #【入力】
    print( f"Year ={Year}") #for debug, output to terminal
    print( f"Area ={Area}") #for debug, output to terminal

    #データベースを引数で指定できるバージョン
    from mydblib2 import my_select

    #SQLの設定 
    # tableに検索するtable名 
    sqlstring =  f"""
        SELECT Month,Temp_mean
        FROM weather
        WHERE Area = '{Area}'
        AND Year = {Year}
        ;
    """
    #webprogデータベースのweatherテーブルのレコードを読み込み
    weather = my_select( "webprog",sqlstring )
    #print( weather)  #for debug, output to terminal
    
    title = f"{Area}の{Year}年の月別平均気温" 

    import matplotlib.pyplot as plt
    import japanize_matplotlib

    plt.plot(weather["Month"],weather["Temp_mean"])
    plt.title( title )
    plt.xlabel("月")
    plt.ylabel("温度")
    plt.savefig("./static/Rei0403-2.png")
    plt.close()

    return render_template(
        "Rei0403-table.html",
        title = title,
        cols = weather.columns,
        table_data = weather.values,
        image = "/static/Rei0403-2.png"        
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)