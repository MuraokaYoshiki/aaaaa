-- q31
CREATE DATABASE if NOT EXISTS dbtest01;
USE dbtest01;

DROP TABLE if EXISTS attendance;
DROP TABLE if EXISTS kamoku;
DROP TABLE if EXISTS gakuseki;

CREATE TABLE gakuseki(
    gakusekiID INT NOT NULL AUTO_INCREMENT, 
    gakusekicode VARCHAR(10) NOT NULL UNIQUE, 
    namae VARCHAR(30) NOT NULL, 
    a_year INT NOT NULL, 
    delflag BOOLEAN default FALSE, 
    lastupdate DATETIME, 
    PRIMARY KEY(gakusekiID)
);

CREATE TABLE kamoku(
    kamokuID INT NOT NULL AUTO_INCREMENT, 
    kamokucode VARCHAR(10) NOT NULL UNIQUE, 
    subjectname VARCHAR(50) NOT NULL, 
    tantou VARCHAR(30) NOT NULL, 
    lastupdate DATETIME, 
    PRIMARY KEY(kamokuID)
);

CREATE TABLE attendance(
    attendanceID INT NOT NULL AUTO_INCREMENT, 
    gakusekicode VARCHAR(10), 
    kamokucode VARCHAR(10), 
    classdate DATE NOT NULL, 
    atdata INT NOT NULL, 
    lastupdate DATETIME, 
    PRIMARY KEY(attendanceID), 
    FOREIGN KEY(gakusekicode)
        REFERENCES gakuseki(gakusekicode)
        ON DELETE CASCADE
        ON UPDATE CASCADE, 
    FOREIGN KEY(kamokucode)
        REFERENCES kamoku(kamokucode)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

DESC gakuseki;
DESC kamoku;
DESC attendance;