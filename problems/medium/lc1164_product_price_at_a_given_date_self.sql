-- solved in 39:10
select p.product_id, ifnull(t.new_price,10) as price
from Products p
left join (

select * from
(select row_number() over (partition by product_id order by change_date desc) as rn,
    product_id, 
    new_price
from Products
where change_date <= "2019-08-16" 
) as a
where rn = 1

) as t
on p.product_id = t.product_id 
group by 1