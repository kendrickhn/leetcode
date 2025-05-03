-- solved in 28:58
select s.request_at as 'Day', round((sum(s.status='cancelled_by_driver')+sum(s.status='cancelled_by_client'))/count(s.id),2) as 'Cancellation Rate'
from Trips s
 join Users as uc
on s.client_id = uc.users_id and uc.role ='client' and uc.banned = 'No'
 join Users as ud
on s.driver_id = ud.users_id and ud.role = 'driver' and ud.banned = 'No'
where s.request_at <= '2013-10-03' and s.request_at >= '2013-10-01'
group by s.request_at
order by 1 