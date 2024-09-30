from flask import Flask,render_template,request

#Flaskのコンストラクタ
app = Flask(__name__)

#ルーティング定義
@app.route("/")
def top():
    #半径の入力フォーム
    return render_template(
        "form_1.html"
    )

import numpy as np
@app.route("/taxi1",methods=["POST"])
def taxi1():
    kyori = float( request.form["kyori"])
    if kyori<=1500:
        ryoukin = 710
    else:
        kukan = np.ceil((kyori-1500)/293)
        ryoukin = 710 + kukan*90
    yakan = np.round( ryoukin*1.3 , -1)
    msg = f"昼間{ryoukin:.0f}  夜間{yakan:.0f}"

    return render_template(
        "message.html",
        title = f"乗車距離{kyori}mの料金",
        message = msg
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)
