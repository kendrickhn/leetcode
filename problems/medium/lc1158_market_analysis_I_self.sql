-- solved in 13:22
select u.user_id as buyer_id, u.join_date, ifnull(count(o.item_id),0) as 'orders_in_2019'
from Orders o 
right join Users u 
on o.buyer_id=u.user_id and YEAR(o.order_date)= '2019'
group by u.user_id 

