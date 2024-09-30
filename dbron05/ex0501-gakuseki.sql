CREATE DATABASE if NOT EXISTS dbron05;
USE dbron05;
DROP table if exists gakuseki;
CREATE TABLE gakuseki(
    gakusekiID INT NOT NULL AUTO_INCREMENT,
    gakusekicode VARCHAR(10) ,
    namae VARCHAR(30),
    ggteacher VARCHAR(30),
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
