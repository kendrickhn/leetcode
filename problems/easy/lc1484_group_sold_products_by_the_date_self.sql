-- solved in 16:39
-- myCode:
-- select sell_date, 
--         sum(c) as num_sold, 
--         group_concat(product order by product asc separator ',') as products
-- from(
-- select sell_date, 
--         product,
--         count(distinct product) as c
-- from Activities
-- group by sell_date, product
-- ) as t
-- group by sell_date

SELECT sell_date, count( DISTINCT product ) as num_sold ,
    GROUP_CONCAT( DISTINCT product order by product ASC separator ',' ) as products
FROM Activities GROUP BY sell_date order by sell_date ASC;