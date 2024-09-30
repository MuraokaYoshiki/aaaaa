CREATE DATABASE if NOT EXISTS dbron05;
USE dbron05;
DROP table if exists seiseki;
CREATE TABLE seiseki(
    seisekiID INT NOT NULL AUTO_INCREMENT,
    gakusekiID INT ,
    season INT,
    kamoku VARCHAR(30),
    score INT,
    PRIMARY KEY(seisekiID),
    FOREIGN KEY(gakusekiID)
        REFERENCES gakuseki(gakusekiID)
        ON DELETE cascade
        ON UPDATE cascade
);
DESC seiseki;
INSERT INTO seiseki
(gakusekiID, season, kamoku,score )
VALUES
  (1,2018,'数学',62),
  (2,2018,'数学',79),
  (3,2018,'数学',0),
  (4,2018,'数学',44),
  (5,2018,'数学',62),
  (1,2018,'英語',56),
  (2,2018,'英語',72),
  (3,2018,'英語',15),
  (4,2018,'英語',71),
  (5,2018,'英語',44),
  (1,2018,'国語',50),
  (2,2018,'国語',100),
  (3,2018,'国語',49),
  (4,2018,'国語',56),
  (5,2018,'国語',76),
  (1,2019,'数学',31),
  (2,2019,'数学',65),
  (3,2019,'数学',14),
  (4,2019,'数学',1),
  (5,2019,'数学',54),
  (1,2019,'英語',46),
  (2,2019,'英語',87),
  (3,2019,'英語',35),
  (4,2019,'英語',21),
  (5,2019,'英語',62),
  (1,2019,'国語',56),
  (2,2019,'国語',51),
  (3,2019,'国語',15),
  (4,2019,'国語',27),
  (5,2019,'国語',28),
  (1,2019,'物理',100),
  (2,2019,'物理',51),
  (3,2019,'物理',44),
  (4,2019,'物理',62),
  (5,2019,'物理',31)
;
SELECT * FROM seiseki;