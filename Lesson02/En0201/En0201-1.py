from flask import Flask,render_template,request
import numpy as np


#Flaskのコンストラクタ
app = Flask(__name__)

@app.route("/")
def top():
    #入力フォーム
    return "タクシー料金計算"


@app.route("/<kyori>")
def taxi(kyori):
    kyori=int(kyori)
    #距離の設定
    if kyori<=1500:
        ryoukin=710
    else:
        #区間
        kukan=np.ceil((kyori-1500)/283)
        #昼間の料金
        ryoukin=710+kukan*90
    #夜間
    yakan=np.round(ryoukin*1.3,decimals=-1)
    #結果の表示
    return render_template(
        "top.html",
        title=f"距離{kyori:.3f}mの時、",
        message=f"昼間{ryoukin}円,夜間{yakan}円"
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)