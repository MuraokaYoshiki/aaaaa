CREATE DATABASE if NOT EXISTS dbron07;
USE dbron07;
DROP table if exists seiseki;
DROP table if exists gakuseki;
CREATE TABLE gakuseki(
    gakusekiID INT NOT NULL AUTO_INCREMENT,
    gakusekicode VARCHAR(10) UNIQUE,
    namae VARCHAR(30),
    ggteacher VARCHAR(30),
    delflag BOOLEAN DEFAULT False,
    lastupdate datetime,
    PRIMARY KEY(gakusekiID)
);
DESC gakuseki;
INSERT INTO gakuseki
(gakusekicode, namae, ggteacher,lastupdate)
VALUES
('H001','宇佐川','広瀬',now()),
('H002','草本','広瀬',now()),
('H003','上米良','広瀬',now()),
('H004','宗本','薬丸',now()),
('H005','千ケ崎','薬丸',now())
;
SELECT * FROM gakuseki;

CREATE TABLE seiseki(
    seisekiID INT NOT NULL AUTO_INCREMENT,
    gakusekicode VARCHAR(10) ,
    season INT,
    kamoku VARCHAR(30),
    score INT,
    lastupdate datetime,
    PRIMARY KEY(seisekiID),
    FOREIGN KEY(gakusekicode)
        REFERENCES gakuseki(gakusekicode)
        ON DELETE cascade
        ON UPDATE cascade
);
DESC seiseki;
INSERT INTO seiseki
(gakusekicode, season, kamoku,score,lastupdate )
VALUES
  ("H001",2018,'数学',62,now()),
  ("H002",2018,'数学',79,now()),
  ("H003",2018,'数学',0,now()),
  ("H004",2018,'数学',44,now()),
  ("H005",2018,'数学',62,now()),
  ("H001",2018,'英語',56,now()),
  ("H002",2018,'英語',72,now()),
  ("H003",2018,'英語',15,now()),
  ("H004",2018,'英語',71,now()),
  ("H005",2018,'英語',44,now()),
  ("H001",2018,'国語',50,now()),
  ("H002",2018,'国語',100,now()),
  ("H003",2018,'国語',49,now()),
  ("H004",2018,'国語',56,now()),
  ("H005",2018,'国語',76,now()),
  ("H001",2019,'数学',31,now()),
  ("H002",2019,'数学',65,now()),
  ("H003",2019,'数学',14,now()),
  ("H004",2019,'数学',1,now()),
  ("H005",2019,'数学',54,now()),
  ("H001",2019,'英語',46,now()),
  ("H002",2019,'英語',87,now()),
  ("H003",2019,'英語',35,now()),
  ("H004",2019,'英語',21,now()),
  ("H005",2019,'英語',62,now()),
  ("H001",2019,'国語',56,now()),
  ("H002",2019,'国語',51,now()),
  ("H003",2019,'国語',15,now()),
  ("H004",2019,'国語',27,now()),
  ("H005",2019,'国語',28,now()),
  ("H001",2019,'物理',100,now()),
  ("H002",2019,'物理',51,now()),
  ("H003",2019,'物理',44,now()),
  ("H004",2019,'物理',62,now()),
  ("H005",2019,'物理',31,now())
;
SELECT * FROM seiseki;
