-- ex0602-3.sql

USE dbron06;

DROP VIEW if exists gaku_sei;
CREATE VIEW gaku_sei AS
    SELECT gakuseki.gakusekiID as gakusekiID,
        gakuseki.gcode as gcode,
        gakuseki.namae as namae,
        gakuseki.ggteacher as ggteacher,
        gakuseki.delflag as delflag,
        seiseki.seisekiID as seisekiID,
        seiseki.acyear as acyear,
        seiseki.kamoku as kamoku ,
        seiseki.score as score
    FROM gakuseki 
    INNER JOIN seiseki
    ON gakuseki.gcode = seiseki.gcode
;

select *
FROM gaku_sei
WHERE gcode = 'H001'
;
