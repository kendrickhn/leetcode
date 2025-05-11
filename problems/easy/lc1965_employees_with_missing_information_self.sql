-- solved in 6:01
select * from
(select employee_id 
from Employees 
where employee_id not in (select employee_id from Salaries)) as e
union
select * from
(select employee_id
from Salaries
where employee_id not in (select employee_id from Employees)) as s
order by 1