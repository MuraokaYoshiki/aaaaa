USE dbron04;
ALTER TABLE meibo
ADD COLUMN delflag boolean not null default False;
DESC meibo
;