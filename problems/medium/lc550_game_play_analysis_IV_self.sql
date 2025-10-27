select round(
    sum(
    case 
    when date_add(f.fd, INTERVAL 1 DAY) = a.event_date then 1
    else 0 
    end
    ) / 
    (select count(distinct player_id) from Activity )
    ,2) as fraction
from Activity a
left join (
    select player_id, min(event_date) as fd from Activity group by 1
) f
on a.player_id = f.player_id