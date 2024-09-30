from flask import Flask,render_template,request
import numpy as np
#Flaskのコンストラクタ
app = Flask(__name__)

#ルーティング定義
@app.route("/")
def top():
    return "ようこそ素数の世界へ"

@app.route("/sosuu/")
def top1():
    prime=np.array([])
    for n in range(2,11):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            prime=np.append(prime,n)

    msg=f"素数は{prime}"            
    return render_template(
        "top.html",
        title=f"10までの素数",
        message=msg
    )
@app.route("/sosuu/<num>")
def top2(num) :
        num=int(num)
        prime=np.array([])
        for n in range(2,num+1):
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                prime=np.append(prime,n)

        msg=f"素数は{prime}"            
        return render_template(
            "top.html",
            title=f"{num}までの素数",
            message=msg
        )
#プログラム起動
app.run(host="localhost",port=5000,debug=True)