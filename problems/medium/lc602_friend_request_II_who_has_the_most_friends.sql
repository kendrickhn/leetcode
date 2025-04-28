# solved in 21:14
select ra.id,
    coalesce(a.added_num,0) + coalesce(r.add_num,0) as num 

from 
(select distinct (requester_id) as id from RequestAccepted 
union 
select distinct (accepter_id) as id from RequestAccepted) as ra

left join 
(select accepter_id as id, 
count(requester_id) as added_num 
from RequestAccepted 
group by 1) as a
on ra.id=a.id

left join
(select requester_id as id, 
count(accepter_id) as add_num
from RequestAccepted
group by 1) as r
on ra.id=r.id

group by 1
order by 2 desc
limit 1