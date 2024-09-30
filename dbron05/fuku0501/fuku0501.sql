-- fuku0501.sql 
CREATE DATABASE if not exists dbron05;
USE dbron05;
DROP TABLE if exists meibo;
--テーブルmeiboの作成と定義
CREATE TABLE meibo 
(
    meiboID int not NULL auto_increment,
    gakuseki varchar(30) not NULL,
    namae varchar(30) not NULL,
    yomi varchar(50),
    acyear int,
    math int,
    eng int,
    PRIMARY KEY (meiboID)
);

DESC meibo;