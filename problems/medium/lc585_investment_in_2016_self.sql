# solved in 9:26
select round(sum(tiv_2016),2) as tiv_2016
from Insurance
where tiv_2015 in (select tiv_2015 from Insurance group by 1 having count(*) > 1)
    and lat in (select lat from Insurance group by lat, lon having count(*) = 1)
    and lon in (select lon from Insurance group by lat, lon having count(*) = 1)