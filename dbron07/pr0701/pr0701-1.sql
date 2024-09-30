-- データベースdbron07が存在しなければ作成
CREATE DATABASE if NOT EXISTS dbron07;

-- dbron07を使う
USE dbron07;

-- seki,studentテーブルが既に存在すれば削除する
DROP table if exists student;
DROP table if exists seki;

-- studentテーブルの定義
CREATE TABLE student(
    studentID INT NOT NULL AUTO_INCREMENT,
    s_code VARCHAR(10) NOT NULL UNIQUE,
    namae VARCHAR(30),
    prefecture VARCHAR(10),
    delflag BOOLEAN default False,
    lastupdate datetime,
    PRIMARY KEY(studentID)
);



-- sekiテーブルの定義
CREATE TABLE seki(
    sekiID INT NOT NULL AUTO_INCREMENT,
    s_code VARCHAR(10) ,
    jcnt INT,
    sekidata INT,
    lastupdate datetime,
    PRIMARY KEY(sekiID),
    FOREIGN KEY(s_code)
        REFERENCES student(s_code)
);

-- student,sekiテーブルの説明 desc
DESC student;
DESC seki;


-- VIEW std_sekiの作成
DROP VIEW if exists std_seki;
CREATE VIEW std_seki AS
    SELECT 
        student.s_code ,
        student.namae ,
        student.prefecture ,
        seki.jcnt ,
        seki.sekidata
    FROM student
    INNER JOIN seki
    ON student.s_code = seki.s_code
; 
DESC std_seki;
