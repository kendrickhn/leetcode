# solved in 19:12 with help 

select 
(select salary as SecondHighestSalary from
(select id, salary, dense_rank() over (order by salary desc) as r from Employee) as t
where r = 2
limit 1) as SecondHighestSalary

