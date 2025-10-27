-- solved in 35:13
select d.name as Department,
        e.name as Employee, 
        e.salary as Salary
from Employee e 

join Department d
on e.departmentId = d.id 

join (select departmentId, 
            dense_rank() over (
                partition by departmentId 
                order by salary desc
            ) as rn, 
            salary 
        from Employee ) t
on t.salary = e.salary and t.departmentId=e.departmentId
where rn <=3
group by e.id


