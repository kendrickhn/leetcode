-- Solved in 2:24:18
with swap as(
select case 
    when mod(id,2) = 1 then id+1
    when mod(id,2) = 0 then id-1
    else 0
    end as id, 
    student
from Seat 
where id < (select max(id) from Seat)

union all

select case 
        when mod(id,2) = 1 then id
        when mod(id,2) = 0 then id-1
        else 0
        end as id, 
        student
from Seat 
where id = (select max(id) from Seat)
) 

select c.id, 
    s.student
from swap c
left join Seat s 
on c.student=s.student
order by c.id
