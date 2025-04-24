Select query_name, 
    round(avg(rating/position),2) as quality, 
    case
        when count(*)= 1 and rating >2 then 0
        when count(*)= 1 and rating <3 then 100
        else round(100* sum(rating<3) / count(rating) ,2)
    end as poor_query_percentage
from Queries
group by query_name;