-- pr0602-2.sql 3つのテーブルを内部結合するビュー
use pr0602;

CREATE VIEW item_cus_sal AS
    SELECT 
        customer.customerID as customerID,
        customer.cname as cname,
        item.iname as iname,
        item.unitprice as unitprice,
        salesdetail.quantity as quantity,
        unitprice * quantity as price,
        salesdetail.salesdate as salesdate
    FROM salesdetail
    INNER JOIN customer
    ON salesdetail.customerID = customer.customerID
    INNER JOIN item
    ON salesdetail.itemcode = item.itemcode
;

SELECT *
FROM item_cus_sal
;
