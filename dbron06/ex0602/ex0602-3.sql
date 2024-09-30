-- ex0602-3.sql

USE dbron06;

DROP VIEW if exists gaku_sei;

#gakus_seiビューの作成


#Viewが正しく動作しているかの，確認
select *
FROM gaku_sei
WHERE gcode = 'H001'
;
