-- ex0701-0.sql  ビューの定義
DROP VIEW if exists gaku_sei ;
CREATE VIEW gaku_sei AS
    SELECT gakuseki.gakusekiID as gakusekiID,
        gakuseki.namae as namae,
        gakuseki.ggteacher as ggteacher,
        gakuseki.delflag as delflag,
        seiseki.seisekiID as seisekiID,
        seiseki.gakusekicode as gakusekicode,
        seiseki.season as season,
        seiseki.kamoku as kamoku,
        seiseki.score as score
FROM seiseki
INNER JOIN gakuseki
ON seiseki.gakusekicode = gakuseki.gakusekicode
;
