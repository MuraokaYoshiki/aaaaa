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

#プログラム起動 ルーティング定義の後に記述
app.run(host="localhost",port=5000,debug=True)
