-- solved in 14:19
select m.manager_id as employee_id, 
        e.name, 
        m.reports_count, 
        m.average_age
from (select reports_to as manager_id,
        count(employee_id) as reports_count, 
        round(avg(age),0) as average_age
    from Employees
    where reports_to is not null
    group by 1) as m
left join Employees e
on m.manager_id=e.employee_id
order by 1