from flask import Flask,render_template

#Flaskのコンストラクタ
app = Flask(__name__)

#ルーティング定義
@app.route("/")
def top():
    return "Hello Flask world"

#http://localhost:5000/samp01/にリクエストが来たときの処理
@app.route("/samp01/")
def top2():
    return "これは，samp01のリクエストです"

#http://localhost:5000/samp01/hiroseとリクエストするときの処理
@app.route("/samp01/<namae>")
def top3(namae):
    return f"あなたの名前は， {namae} です。"

@app.route("/samp02/<namae>/<age>")
def top4(namae,age):
    return f"あなたの名前は {namae}，年齢は{age} です。"

#render_templateの例1 
@app.route("/temp01")
def temp01():
    return render_template(
        #templateのHTMLファイル名を指定
        "top.html"
    )

#render_templateの例1 
@app.route("/temp02")
def temp02():
    return render_template(
        #templateのHTMLファイル名を指定
        "top2.html",
        #top2.htmlに引数を渡す
        title = "render_templateの例２",
        message="top2.htmlにtitleとmessageを引数で受け渡す事例"
    )

#render_templateの例２
@app.route("/temp02/<namae>")
def temp02_namae(namae):
    return render_template(
        #templateのHTMLファイル名を指定
        "top2.html",
        #top2.htmlに引数を渡す
        title = f"こんにちは{namae}さん",
        message="Webプログラミングについて、ずいぶん知識が増えましたね"
    )

#render_templateの例3
#URLで半径を指定し、級の体積と表面積を表示するプログラム
import numpy as np
@app.route("/calc/<r>")
def calc_r(r):
    r = float(r)
    v = 4 / 3 * np.pi * r ** 3
    s = 4 * np.pi * r ** 2

    msg = f"表面積は{s:.3f}  体積は{v:.3f}"
    return render_template(
        "top2.html",
        title = f"半径{r}のとき",
        message = msg
    )

#render_template【演習】
#URLで乗車距離を入力し、タクシー料金を表示するプログラム
#初乗り1.5kmまで710円、以降293mごとに90円、夜間は昼間の1.3倍10円未満四捨五入
#【入力】

#URLの引数を素因数分解し表示するプログラム
@app.route("/prime_fact/<num>")
def prime_fact(num):
    n = int(num)
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    return render_template(
        "top2.html",
        title = f"{num}の素因数分解",
        message = f"{factors}の積となる"
    )

#プログラム起動 ルーティング定義の後に記述
app.run(host="localhost",port=5000,debug=True)
