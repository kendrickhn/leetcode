-- solved in 01:13:36
select person_name
from (
    select turn, 
        person_name, sum(weight) over (order by turn) > 1000 as cooked
        from Queue
        order by turn
) as bus
where cooked = 0
order by turn desc
limit 1
