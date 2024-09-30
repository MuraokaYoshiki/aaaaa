-- 演習１　pr0601.sql
USE sampledb;

-- (1)
DROP VIEW if exists order_summary;
CREATE VIEW order_summary AS
    SELECT e_usr.user_id as user_id, 
    e_usr.l_name as l_name, 
    e_usr.f_name as f_name, 
    e_ordermain.order_date as order_date,
    e_product.p_name as p_name,
    e_product.price as price,
    e_orderdetail.quantity as quantitiy,
    price * quantity as s_total
    FROM e_usr
    INNER JOIN e_ordermain
    ON e_usr.user_id = e_ordermain.user_id
    INNER JOIN e_orderdetail
    ON e_ordermain.po_id = e_orderdetail.po_id
    INNER JOIN e_product
    ON e_orderdetail.p_id = e_product.p_id
;

-- (2)
SELECT *
FROM order_sumamry
;

-- (3)
SELECT user_id,l_name,f_name,SUM(s_total) as goukei
FROM order_summary
GROUP BY user_id
;

