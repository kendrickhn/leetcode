-- solved in 14:44
select * from 
(SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
UNION ALL
SELECT product_id, 'store2', store2
FROM Products
UNION ALL
SELECT product_id, 'store3', store3
FROM Products) s
where price is not null 
order by 1;