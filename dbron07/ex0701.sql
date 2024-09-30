CREATE DATABASE if NOT EXISTS dbron07;
USE dbron07;
DROP table if exists gakuseki;
CREATE TABLE gakuseki(
    gakusekiID INT NOT NULL AUTO_INCREMENT,
    gakusekicode VARCHAR(10) UNIQUE,
    namae VARCHAR(30),
    ggteacher VARCHAR(30),
    delflag BOOLEAN default Falae,
    lastupdate datetime,
    PRIMARY KEY(gakusekiID)
);
DESC gakuseki;
INSERT INTO gakuseki
(gakusekicode, namae, ggteacher)
VALUES
('H001','宇佐川','広瀬'),
('H002','草本','広瀬'),
('H003','上米良','広瀬'),
('H004','宗本','薬丸'),
('H005','千ケ崎','薬丸')
;
SELECT * FROM gakuseki;

DROP table if exists seiseki;
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
(gakusekicode, season, kamoku,score )
VALUES
  ("H001",2018,'数学',62),
  ("H002",2018,'数学',79),
  ("H003",2018,'数学',0),
  ("H004",2018,'数学',44),
  ("H005",2018,'数学',62),
  ("H001",2018,'英語',56),
  ("H002",2018,'英語',72),
  ("H003",2018,'英語',15),
  ("H004",2018,'英語',71),
  ("H005",2018,'英語',44),
  ("H001",2018,'国語',50),
  ("H002",2018,'国語',100),
  ("H003",2018,'国語',49),
  ("H004",2018,'国語',56),
  ("H005",2018,'国語',76),
  ("H001",2019,'数学',31),
  ("H002",2019,'数学',65),
  ("H003",2019,'数学',14),
  ("H004",2019,'数学',1),
  ("H005",2019,'数学',54),
  ("H001",2019,'英語',46),
  ("H002",2019,'英語',87),
  ("H003",2019,'英語',35),
  ("H004",2019,'英語',21),
  ("H005",2019,'英語',62),
  ("H001",2019,'国語',56),
  ("H002",2019,'国語',51),
  ("H003",2019,'国語',15),
  ("H004",2019,'国語',27),
  ("H005",2019,'国語',28),
  ("H001",2019,'物理',100),
  ("H002",2019,'物理',51),
  ("H003",2019,'物理',44),
  ("H004",2019,'物理',62),
  ("H005",2019,'物理',31)
;
SELECT * FROM seiseki;
