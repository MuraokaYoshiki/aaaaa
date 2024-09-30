-- fuku0701.sql
-- (1) 
USE sampledb;
DROP VIEW if exits shop_sales;
CREATE VIEW shop_sales AS
    SELECT uri_shop.s_id as s_id,
        uri_sales.s_date as s_date,
        uri_sales.s_value as s_value,
        uri_shop.s_name as s_name
    FROM uri_sales
    INNER JOIN uri_shop
    ON uri_sales.s_id = uri_shop.s_id
;
-- (2)
SELECT s_id,s_name,sum(s_value) as goukei1
FROM shop_sales
GROUP BY s_id
;
-- (3)
SELECT s_date ,sum(s_value) as goukei2
FROM shop_sales
GROUP BY s_date
;