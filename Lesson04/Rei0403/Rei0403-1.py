#En0401-1　Flaskモジュールで，DBアクセス&データ分析
#このプログラムは，グラフファイルを出力するので，実行するディレクトリが重要
#En0401.pyが存在するディレクトリを，カレントディレクトリとして実行する

from flask import Flask,render_template 
#Flaskのコンストラクタ
app = Flask(__name__ ,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    return render_template( "【入力】",
        title = "各地の年間平均気温",
        message = "各地の平均気温を表示するには，http://localhost:5000/form "
    ) 

#地点と年度を選択するフォーム
@app.route("/form")
def top2():
    return render_template(  "【入力】",
        title="地域，年度選択フォーム"
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)