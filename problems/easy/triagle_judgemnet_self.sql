-- solved in 3:55
select x,y,z, 
case when z < (x+y) and x < (y+z) and y< (z+x) then "Yes" 
    else "No" 
    end as triangle 
from Triangle