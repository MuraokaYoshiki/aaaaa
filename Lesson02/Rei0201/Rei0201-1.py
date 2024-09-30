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
    return "これは、samp01のリクエストです"

#プログラム起動 ルーティング定義の後に記述
app.run(host="localhost",port=5000,debug=True)
