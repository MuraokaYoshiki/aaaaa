from flask import Flask, render_template, request
#Flask のコンストラクタ
app = Flask(__name__ ,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    return render_template( "TS3-top-T122142.html",
        title = "Webプログラミング問題3 【T122142】",
        message = """
            諏訪の年ごとの平均気温グラフ http://localhost:5000/Suwa
            特定地区の平均気温グラフ http://localhost:5000/Area/{地区名}
            フォームに地区と表示項目選択 http://localhost:5000/form
            """
    ) 

@app.route("/Suwa")
def top2():
    #データベースを引数で指定できるバージョン
    from mydblib2 import my_select
    
    #SQL の設定
    sqlstring = f"""
        SELECT Year,Temp_mean FROM weather WHERE Area = 'Suwa';
    """
    #wptest データベースの weather テーブルのレコードを読み込み
    weather = my_select("wptest", sqlstring).groupby("Year").mean(numeric_only=True)
    print(f"weather\n{weather}") #for debug, output to terminal
    
    title = "SuwaのTemp_mean"

    import matplotlib.pyplot as plt
    import japanize_matplotlib

    plt.plot(weather.index, weather.values, color="#377eb8")
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Celsius")
    plt.savefig("./static/TS32-T122142.png")
    plt.close()
    
    return render_template(
        "TS3-result-T122142.html",
        title = title,
        image = "/static/TS32-T122142.png"
)

@app.route("/Area/<Area>")
def top3(Area):
    #データベースを引数で指定できるバージョン
    from mydblib2 import my_select
    
    #SQL の設定
    sqlstring = f"""
        SELECT Year,Temp_mean FROM weather WHERE Area = '{Area}';
    """
    #wptest データベースの weather テーブルのレコードを読み込み
    weather = my_select("wptest", sqlstring).groupby("Year").mean(numeric_only=True)
    print(f"weather\n{weather}") #for debug, output to terminal
    
    title = f"{Area}のTemp_mean"

    import matplotlib.pyplot as plt
    import japanize_matplotlib

    plt.plot(weather.index, weather.values, color="#377eb8")
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Celsius")
    plt.savefig("./static/TS33-T122142.png")
    plt.close()
    
    return render_template(
        "TS3-result-T122142.html",
        title = title,
        image = "/static/TS33-T122142.png"
)

@app.route("/form")
def top4():
    return render_template(
        "TS3-form-T122142.html",
        title = "地域, 気象データ選択フォーム",
)


@app.route("/search",methods=["POST"])
def top5():
    #form 変数を受け取り
    Area = request.form["Area"]
    Data = request.form["Data"]
    # print( f"Area ={Area}") #for debug, output to terminal
    # print( f"Data ={Data}") #for debug, output to terminal

    #データベースを引数で指定できるバージョン
    from mydblib2 import my_select
    
    #SQL の設定
    # table に検索する table 名
    sqlstring = f"""
        SELECT Year,{Data} FROM weather WHERE Area = '{Area}';
    """

    #wptest データベースの weather テーブルのレコードを読み込み
    weather = my_select("wptest", sqlstring).groupby("Year").mean(numeric_only=True)
    # print(f"weather\n{weather}") #for debug, output to terminal
    
    title = f"{Area}の{Data}"
    
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    
    plt.plot(weather.index, weather.values)
    
    unit = {"Temp_mean":"Celsius", "Temp_max":"Celsius", "Temp_min":"Celsius", "Precipitation":"mm", "Sunshine":"Hours"}
    
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(unit[Data])
    plt.savefig("./static/TS34-T122142.png")
    plt.close()
    
    return render_template(
        "TS3-result-T122142.html",
        title = title,
        image = "/static/TS34-T122142.png"
)

#プログラム起動
app.run(host="localhost",port=5000,debug=True)