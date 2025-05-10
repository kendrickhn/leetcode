-- solved in 11:02
with t as 
(select stock_name, operation, sum(price) as price
from Stocks 
group by stock_name, operation)

select b.stock_name, s.price - b.price as capital_gain_loss 
from 
(select stock_name, price from t where operation = 'Buy') as b
left join 
(select stock_name, price from t where operation = 'Sell') as s
on b.stock_name = s.stock_name

