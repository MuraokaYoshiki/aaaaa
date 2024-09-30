#pr0602.py 　3つのCSVファイルをテーブルにインポートするプログラム

from MyDatabase import my_open , my_query , my_close
import pandas as pd

#Data Source Nameのパラメータを辞書型変数で定義しオープン
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'pr0602' #オープンするデータベース名
}
dbcon,cur = my_open( **dsn )

#2つのファイル名をlist変数として保存
filename = ["./pr0602-item.csv","./pr0602-customer.csv","./pr0602-salesdetail.csv"]

#現在の日時を取得
import datetime
dt_now = datetime.datetime.now()

#2つのファイルを処理するための繰り返し処理 fnにファイル名が入る
for fn in filename:

    #ファイルオープン 先頭行をheaderとして
    df = pd.read_csv( fn ,header=0)

    #recsetは，DataFrameのため，indexとrowdataをペアで取得する
    for ind,rowdata in df.iterrows():

        #レコードを挿入するSQL文をそれぞれ定義する
        if fn == "./pr0602-item.csv" :
            #itemテーブルの場合
            sqlstring = f"""
                INSERT INTO item
                (itemcode,iname,unitprice,maker,lastupdate)
                values
                ('{rowdata.itemcode}','{rowdata.iname}',{rowdata.unitprice},'{rowdata.maker}','{dt_now}')
                ;
            """
        elif fn == "./pr0602-customer.csv" :
            #customerテーブルの場合
            sqlstring = f"""
                INSERT INTO customer
                (cname,caddress,tel,lastupdate)
                values
                ('{rowdata.cname}','{rowdata.caddress}','{rowdata.tel}','{dt_now}')
                ;
            """
        else:
            #salesdetailテーブルの場合
            sqlstring = f"""
                INSERT INTO salesdetail
                (itemcode,customerID,quantity,salesdate,lastupdate)
                values
                ('{rowdata.itemcode}',{rowdata.customerID},{rowdata.quantity},'{rowdata.salesdate}','{dt_now}')
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
