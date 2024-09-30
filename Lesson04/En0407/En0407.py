from flask import Flask,render_template,request
from scipy import stats 
import numpy as np
#Flaskのコンストラクタ
app = Flask(__name__ ,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    return render_template( "En0407.html",
        title = "平均気温分析ページ",
        message = "平均気温を比較する地域と年代を選択してください."
    ) 



#地点と年度を選択するフォーム
@app.route("/search",methods=["POST"])
def top2():
    #form変数を受け取り
    Year = request.form["year"]
    Area = request.form["Area"]
    Year1 = request.form["year1"]
    Area1 = request.form["Area1"]

    #【入力】
    print( f"Year ={Year}") #for debug, output to terminal
    print( f"Area ={Area}") #for debug, output to terminal
    print( f"Year1 ={Year1}") #for debug, output to terminal
    print( f"Area1 ={Area1}") #for debug, output to terminal

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
    sqlstring1 =  f"""
        SELECT Month,Temp_mean
        FROM weather
        WHERE Area = '{Area1}'
        AND Year = {Year1}
        ;
    """
    #webprogデータベースのweatherテーブルのレコードを読み込み
    weather  = my_select( "webprog",sqlstring )
    print(weather)
    weather1 = my_select( "webprog",sqlstring1 ) 
    print(weather1)
    #print( weather)  #for debug, output to terminal
    title = f"{Area}{Year}年代と{Area1}{Year1}年代の比較"
    print(weather["Temp_mean"])
    print(type(weather["Temp_mean"]))
    
    ans1,ans2 = stats.ttest_ind(weather["Temp_mean"],weather1["Temp_mean"])
    print("一元配置分散分析：",ans2)


    import matplotlib.pyplot as plt
    import japanize_matplotlib

    plt.plot(weather["Month"],weather["Temp_mean"])
    plt.plot(weather1["Month"],weather1["Temp_mean"])
    plt.title( title )
    plt.xlabel("月")
    plt.ylabel("温度")
    plt.savefig("./static/En0407.png")
    plt.close()
    
    if ans2 > 0.05:
        p = "有意差はない"

    return render_template(
        "En0407-1.html",
        title = title,
        Month = weather.columns[0],
        data = Area + Year + "年代",
        data1 = Area1 + Year1 + "年代",
        cols = weather.columns,
        temp = weather.values,
        temp1 = weather1.values,
        ans = ans2,
        p = p,
        image = "/static/En0407.png"
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)