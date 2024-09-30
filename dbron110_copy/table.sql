-- 外部キー制約を無効にする
SET FOREIGN_KEY_CHECKS = 0;

-- テーブルが存在すれば削除する
DROP TABLE IF EXISTS gakusekiss;
DROP TABLE IF EXISTS health_records;
DROP TABLE IF EXISTS activity_records;
DROP TABLE IF EXISTS infection_records;
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS records;

-- 外部キー制約を有効にする
SET FOREIGN_KEY_CHECKS = 1;

-- テーブルの再作成
CREATE TABLE gakusekiss (
    gakuseki_ID varchar(15) NOT NULL PRIMARY KEY,
    namae VARCHAR(30) NOT NULL,
    yakuwari ENUM('学生', '教員','職員', '管理者') NOT NULL,
    email VARCHAR(100) NOT NULL,
    loginpass VARCHAR(100) NOT NULL
);

CREATE TABLE health_records (
    record_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    gakuseki_ID varchar(15) NOT NULL,
    months INT NOT NULL,
    days INT NOT NULL,
    zikan ENUM('AM','PM'),
    bodytemperature float NOT NULL,
    joint_pain BOOLEAN NOT NULL,
    malaise BOOLEAN NOT NULL,
    headache BOOLEAN NOT NULL,
    sore_throat BOOLEAN NOT NULL,
    shortness_breath BOOLEAN NOT NULL,
    Cough BOOLEAN NOT NULL,
    Nausea BOOLEAN NOT NULL,
    Abdominal_pain BOOLEAN NOT NULL,
    Taste_disorder BOOLEAN NOT NULL,
    Olfactory_disorder BOOLEAN NOT NULL,
    sneeze BOOLEAN NOT NULL,
    FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
);

CREATE TABLE activity_records (
    activity_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    gakuseki_ID varchar(15) NOT NULL,
    hiduke DATETIME NOT NULL,
    basyo VARCHAR(50) NOT NULL,
    way varchar(50) NOT NULL,
    departure varchar(50) NOT NULL,
    arrive varchar(50) NOT NULL,
    accompany varchar(50) NOT NULL,
    acc_number int NOT NULL,
    FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
);

CREATE TABLE infection_records (
    infection_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    gakuseki_ID varchar(15) NOT NULL,
    months INT NOT NULL,
    days INT NOT NULL,
    yakuwari ENUM('感染', '濃厚接触者') NOT NULL,
    FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
);

CREATE TABLE notifications (
    notification_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    gakuseki_ID varchar(15) NOT NULL,
    months INT NOT NULL,
    days INT NOT NULL,
    FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
);

CREATE TABLE records (
    record_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    gakuseki_ID varchar(15) NOT NULL,
    months INT NOT NULL,
    days INT NOT NULL,
    zikan ENUM('AM', 'PM') NOT NULL,
    bodytemperature float NOT NULL,
    joint_pain BOOLEAN NOT NULL,
    malaise BOOLEAN NOT NULL,
    headache BOOLEAN NOT NULL,
    sore_throat BOOLEAN NOT NULL,
    shortness_breath BOOLEAN NOT NULL,
    Cough BOOLEAN NOT NULL,
    Nausea BOOLEAN NOT NULL,
    Abdominal_pain BOOLEAN NOT NULL,
    Taste_disorder BOOLEAN NOT NULL,
    Olfactory_disorder BOOLEAN NOT NULL,
    infection BOOLEAN NOT NULL,
    close_contact BOOLEAN NOT NULL,
    FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
);

-- テーブルの構造を確認
DESC gakusekiss;
DESC health_records;
DESC activity_records;
DESC infection_records;
DESC notifications;
DESC records;

-- 使用するデータベースを指定
USE dbron110;

-- gakusekiss テーブルにデータを挿入
INSERT INTO gakusekiss (gakuseki_ID, namae, yakuwari, email, loginpass)
VALUES ('T000000', 'ad', '管理者', 'T122142@ed.sus.ac.jp', '1234');
