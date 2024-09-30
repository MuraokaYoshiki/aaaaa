-- データベースを作成し、使用する
CREATE DATABASE IF NOT EXISTS dbron05;
USE dbron05;

-- 既存のテーブルがある場合、削除する
DROP TABLE IF EXISTS meibo_2nen;
DROP TABLE IF EXISTS meibo_3nen;
DROP TABLE IF EXISTS meibo_gakusei;
DROP TABLE IF EXISTS meibo;

-- メインの名簿テーブルを作成
CREATE TABLE meibo(
    meiboID INT NOT NULL AUTO_INCREMENT,
    gakuseki VARCHAR(10) NOT NULL,
    acyear INT,
    math INT,
    eng INT,            
    mtea VARCHAR(30),   /* 数学教師 */
    etea VARCHAR(30),   /* 英語教師 */
    PRIMARY KEY(meiboID),
    UNIQUE (gakuseki)
) ENGINE InnoDB;

-- 2年生の名簿テーブルを作成
CREATE TABLE meibo_2nen(
    meiboID INT NOT NULL,
    gakuseki VARCHAR(10) NOT NULL, 
    phy INT,            /* 物理 */
    ptea VARCHAR(30),   /* 物理教師 */
    PRIMARY KEY (meiboID),
    FOREIGN KEY (gakuseki) REFERENCES meibo(gakuseki)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE InnoDB;

-- 3年生の名簿テーブルを作成
CREATE TABLE meibo_3nen(
    gakuseki VARCHAR(10) NOT NULL,
    zemi INT,           /* ゼミ研 */
    ztea VARCHAR(30),   /* ゼミ研教師 */
    PRIMARY KEY (gakuseki),
    FOREIGN KEY (gakuseki) REFERENCES meibo(gakuseki)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE InnoDB;

-- 学生情報の名簿テーブルを作成
CREATE TABLE meibo_gakusei(
    gakuseki VARCHAR(10) NOT NULL,
    namae VARCHAR(30) NOT NULL,
    yomi VARCHAR(50),
    Bplace VARCHAR(30), /* 出身 */
    Birth VARCHAR(30),  /* 生年月日 */
    PRIMARY KEY (gakuseki),
    FOREIGN KEY (gakuseki) REFERENCES meibo(gakuseki)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE InnoDB;

-- テーブル構造の確認
DESC meibo;
DESC meibo_2nen;
DESC meibo_3nen;
DESC meibo_gakusei;
