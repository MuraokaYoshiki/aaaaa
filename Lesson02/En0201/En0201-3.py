from flask import Flask,render_template,request
import numpy as np
#Flaskのコンストラクタ
app = Flask(__name__)

#ルーティング定義
@app.route("/")
def top():
    return "ようこそ素因数分解の世界へ"

@app.route("/prime_fact/<num>")
def top1(num):
        num=int(num)
        f=num
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
            "top.html",
            title=f"{f}までの素因数分解",
            message=msg
        )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)