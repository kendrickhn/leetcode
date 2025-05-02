--solved in 2:16
select score, dense_rank() over (order by score desc) as 'rank' 
from Scores