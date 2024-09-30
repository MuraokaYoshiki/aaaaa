from flask import Flask,render_template,request
import numpy as np
import random

#Flaskのコンストラクタ
app = Flask(__name__)

#ルーティング定義
@app.route("/")
def top():
    #入力フォーム
    return render_template(
        "top.html"
    )

@app.route("/taxi",methods=["post"])
def taxi():
    kyori=int(request.form["kyori"])
    jikan=int(request.form["jikan"])
    #距離の設定
    if kyori<=1500:
        ryoukin=710
    else:
        #区間
        kukan=np.ceil((kyori-1500)/283)
        #昼間の料金
        ryoukin=710+kukan*90
    #夜間
    if jikan==23 or (0 <= jikan <= 5):
        ryoukin=np.round(ryoukin*1.3,decimals=-1)

    #結果の表示
    return render_template(
        "message.html",
        title=f"距離{kyori:.0f}mの時、",
        message=f"料金：{ryoukin:.0f}円"
    )

@app.route("/prime",methods=["post"])
def prime():
        num=int(request.form["num"])
        prime=np.array([])
        for n in range(2,num+1):
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                prime=np.append(prime,n)

        msg=f"素数は{prime}"            
        return render_template(
            "message.html",
            title=f"{num}までの素数",
            message=msg
        )

@app.route("/prime_fact",methods=["post"])
def prime_fact() :
        num=int(request.form["num"])
        til=f"{num}までの素因数分解"
        i=2
        factors=np.array([])
        while i*i <=num:
            if num%i:
                i+=1
            else:
                 num//=i
                 factors=np.append(factors,i)
        if num>1:
             factors=np.append(factors,num)        

        msg=f"素因数分解は{factors}"            
        return render_template(
            "message.html",
            title=til,
            message=msg
        )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)