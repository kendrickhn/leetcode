-- solved in 19:43
select t.transaction_date, ifnull(o.odd_sum,0) as odd_sum,ifnull(e.even_sum,0) as even_sum
from transactions t
left join 
(select transaction_date, sum(amount) as odd_sum
from transactions 
where mod(amount,2)=1 
group by 1) o
on t.transaction_date=o.transaction_date
left join
(select transaction_date, sum(amount) as even_sum
from transactions 
where mod(amount,2)=0 
group by 1) e
on t.transaction_date=e.transaction_date
group by 1
order by 1