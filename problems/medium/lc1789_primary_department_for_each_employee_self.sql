select distinct e.employee_id, 
        case 
        when p.department_id is not null then p.department_id 
        else e.department_id
        end as department_id

from Employee as e
left join (select employee_id, 
                department_id
            from Employee 
            where primary_flag = 'Y') as p
on e.employee_id=p.employee_id