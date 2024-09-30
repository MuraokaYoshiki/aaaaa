-- 問題1　q1-T122142.sql

USE sampledb;
-- (1)
SELECT *
FROM quest
WHERE prefecture='東京都' AND gender='男'
;

-- (2)
SELECT *
FROM post_area
WHERE city IN('茅野市','諏訪市')
;

-- (3)
SELECT city, COUNT(postnumber) AS pcnt
FROM post_area
WHERE city IN('茅野市','諏訪市')
GROUP BY city
;

-- (4)
SELECT *
FROM uri_sales
INNER JOIN uri_shop
ON  uri_sales.s_id = uri_shop.s_id
;

-- (5)
DROP VIEW if EXISTS shop_sales;
CREATE VIEW shop_sales AS
	SELECT uri_shop.s_id,
		uri_shop.s_name,
		uri_sales.s_date,
		uri_sales.s_value
	FROM uri_shop
	INNER JOIN uri_sales
	ON uri_shop.s_id = uri_sales.s_id
;

SELECT *
FROM shop_sales
;


-- (6)
SELECT s_name, SUM(s_value) AS total
FROM shop_sales
WHERE s_name LIKE '%花町%'
GROUP BY s_name
;

