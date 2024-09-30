-- q33
CREATE DATABASE if NOT EXISTS dbtest01;
USE dbtest01;

DROP VIEW if EXISTS ga_ka_at;
CREATE VIEW ga_ka_at AS 
    SELECT attendance.attendanceID as attendanceID, 
        gakuseki.gakusekicode as gakusekicode, 
        kamoku.kamokucode as kamokucode, 
        attendance.classdate as classdate, 
        attendance.atdata as atdata, 
        gakuseki.gakusekiID as gakusekiID, 
        gakuseki.namae as namae, 
        gakuseki.a_year as a_year, 
        gakuseki.delflag as delflag, 
        kamoku.kamokuID as kamokuID, 
        kamoku.subjectname as subjectname, 
        kamoku.tantou as tantou
    FROM (attendance INNEr JOIN gakuseki ON attendance.gakusekicode = gakuseki.gakusekicode) 
    INNER JOIN kamoku ON attendance.kamokucode = kamoku.kamokucode
;

SELECT * FROM ga_ka_at WHERE subjectname='DB論' ORDER BY gakusekiID, classdate ASC;