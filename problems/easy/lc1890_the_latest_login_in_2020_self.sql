-- solved in 1:41
select user_id, max(time_stamp) as last_stamp
from Logins
where YEAR(time_stamp) = '2020'
group by 1 