-- solved in 1:03
select email 
from Person 
group by 1
having count(id)>1;
