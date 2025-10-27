-- solved in 3:55
select distinct l1.num as ConsecutiveNums 
from Logs l1 
left join ( select id+1 as id, num from Logs) as l2
on l1.id=l2.id
left join ( select id+2 as id, num from Logs) as l3
on l1.id=l3.id
where l1.num=l2.num and l1.num=l3.num;