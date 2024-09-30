-- 例題2　ex0602-1.sql

CREATE DATABASE if not EXISTS dbron06;
use dbron06;
DROP TABLE if EXISTS seiseki;
DROP TABLE if EXISTS gakuseki;

CREATE TABLE gakuseki (
    gakusekiID int not NULL AUTO_INCREMENT,
    gcode VARCHAR(10) not NULL UNIQUE,
    namae VARCHAR(30),
    ggteacher VARCHAR(30),
    updated DATETIME,
    delflag BOOLEAN DEFAULT False,
    PRIMARY KEY( gakusekiID )    
);

CREATE TABLE seiseki (
    seisekiID int not NULL AUTO_INCREMENT,
    gcode VARCHAR(10),
    acyear int,
    kamoku VARCHAR(50),
    score int,
    updated DATETIME,
    PRIMARY KEY( seisekiID ),
    FOREIGN KEY ( gcode )
        REFERENCES gakuseki( gcode )
        ON DELETE CASCADE
        ON UPDATE CASCADE

);

DESC gakuseki;
DESC seiseki;
