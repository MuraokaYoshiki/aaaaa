from MyDatabase import my_open , my_query , my_close
import pandas as pd

#Data Source Nameのパラメータを辞書型変数で定義しオープン
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbron07' #オープンするデータベース名
}
dbcon,cur = my_open( **dsn )

#2つのファイル名をlist変数として保存
filename = ["./student.csv"]

#現在の日時を取得
import datetime
dt_now = datetime.datetime.now()

for fn in filename:

    #ファイルオープン 先頭行をheaderとして
    df = pd.read_csv(fn ,header=0)

    #recsetは，DataFrameのため，indexとrowdataをペアで取得する
    for ind,rowdata in df.iterrows():
        #seisekiテーブルの場合
        sqlstring = f"""
            INSERT INTO student
            (s_code,namae,prefecture,lastupdate)
            values
            ('{rowdata[0]}','{rowdata[1]}','{rowdata[2]}','{dt_now}')
            ;
        """
        #クエリー実行
        my_query(sqlstring, cur)

    #INSERT文を実行するループが終了し，結果をフィードバック
    print( f"{fn}を{len( df )}レコードを新規挿入しました")

    #テーブルに書き込み
    dbcon.commit()

#カーソルとDBコンソールのクローズ
my_close(dbcon, cur)


