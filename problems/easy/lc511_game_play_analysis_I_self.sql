select player_id, event_date as first_login
from (select player_id, row_number() over (partition by player_id order by event_date) as rn, event_date
from Activity) as t
where rn=1
