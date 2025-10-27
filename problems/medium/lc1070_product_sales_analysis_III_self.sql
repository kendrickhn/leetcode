select s.product_id, 
        s.year as first_year,
        s.quantity, 
        s.price
from Sales s
join (select product_id, min(year) as year from Sales group by 1) f
on s.product_id = f.product_id and s.year = f.year 
