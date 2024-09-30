import mysql.connector
from mysql.connector import errorcode

# データベース接続の設定
dsn = {
    'host': '172.30.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'dbron110'
}

#gakusekissテーブル作成のSQL文
create_gakusekiss_table_query = """
CREATE TABLE IF NOT EXISTS gakusekiss (
    gakuseki_ID VARCHAR(10) PRIMARY KEY,
    namae VARCHAR(100) NOT NULL,
    yakuwari VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    loginpass VARCHAR(100) NOT NULL
);
"""

#notificationsテーブル作成のSQL文
create_notifications_table_query = """
CREATE TABLE IF NOT EXISTS notifications (
    notification_ID INT AUTO_INCREMENT PRIMARY KEY,
    gakuseki_ID VARCHAR(10) NOT NULL,
    namae VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    sent BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
);
"""
#管理者の情報
admin_data = {
    'gakuseki_ID': 'T000000',
    'namae': '管理者',
    'yakuwari': '管理者',
    'email': 'T000000@ed.sus.ac.jp',
    'loginpass': '1234'
}
# 管理者情報を挿入するSQL文
insert_admin_query = """
INSERT INTO gakusekiss (gakuseki_ID, namae, yakuwari, email, loginpass)
VALUES (%(gakuseki_ID)s, %(namae)s, %(yakuwari)s, %(email)s, %(loginpass)s)
ON DUPLICATE KEY UPDATE
    namae = VALUES(namae),
    yakuwari = VALUES(yakuwari),
    email = VALUES(email),
    loginpass = VALUES(loginpass);
"""

try:
    # データベースに接続
    cnx = mysql.connector.connect(**dsn)
    cursor = cnx.cursor()

    # テーブルを作成
    cursor.execute(create_gakusekiss_table_query)
    print("Table `gakusekiss` created successfully.")
    cursor.execute(create_notifications_table_query)
    print("Table `notifications` created successfully.")

    # 管理者情報を挿入
    cursor.execute(insert_admin_query, admin_data)
    cnx.commit()
    print("Admin information inserted successfully.")

    # 接続を閉じる
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
