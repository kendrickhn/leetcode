select product_id, product_name 
from Product 
where product_id in (select distinct product_id from Sales where sale_date between '2019-01-01' and '2019-03-31')
and product_id not in (select distinct product_id from Sales where not sale_date between '2019-01-01' and '2019-03-31')


-- SELECT DISTINCT p.product_id, p.product_name
-- FROM Sales s
-- LEFT JOIN Product p ON p.product_id = s.product_id
-- GROUP BY p.product_id
-- HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'