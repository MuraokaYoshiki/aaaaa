-- 問題２(2)

USE dbtest01;

ALTER TABLE uriage
    ADD cancelflag BOOLEAN default False,
    ADD lastupdate datetime;

DESC uriage;
