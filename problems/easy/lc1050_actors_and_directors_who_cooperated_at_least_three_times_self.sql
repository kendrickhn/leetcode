# solved in 4:39
select actor_id, director_id 
from
(select actor_id, director_id, count(director_id)
from ActorDirector 
group by 1, 2
having count(director_id) > 2) t
