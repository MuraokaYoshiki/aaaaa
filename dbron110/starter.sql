/*手順を記す。これからの流れは全てHeidSQLで行う

1.CREATE DATABASE if NOT EXISTS dbron110;を実行

2.1度HeidSQLを閉じ、再度開いてデータベースをsampledbからdbron110に変える

3.下のコードを実行。コメントはエラーが出るので消しておく

USE dbron110;
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS gakusekiss;
DROP TABLE IF EXISTS records;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE gakusekiss (
    gakuseki_ID varchar(15) NOT NULL PRIMARY KEY,
    namae VARCHAR(30) NOT NULL,
    yakuwari ENUM('学生', '教員','職員', '管理者') NOT NULL,
    email VARCHAR(100) NOT NULL,
    loginpass VARCHAR(100) NOT NULL
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

INSERT INTO gakusekiss (gakuseki_ID, namae, yakuwari, email, loginpass)
VALUES ('T000000', 'ad', '管理者', 'T000000@ed.sus.ac.jp', '1234');

*/

--最初に管理者を定義するクエリです

-- 外部キー制約を無効にする
SET FOREIGN_KEY_CHECKS = 0;

-- テーブルが存在すれば削除する
DROP TABLE IF EXISTS gakusekiss;
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

-- gakusekiss テーブルにデータを挿入
INSERT INTO gakusekiss (gakuseki_ID, namae, yakuwari, email, loginpass)
VALUES ('T000000', 'ad', '管理者', 'T000000@ed.sus.ac.jp', '1234');