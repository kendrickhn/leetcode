-- solved in 1:86
select e.name as Employee 
from Employee e
join Employee m 
on e.managerId=m.id 
where e.salary > m.salary and m.salary is not null; 
