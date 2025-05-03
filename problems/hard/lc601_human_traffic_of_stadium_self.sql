-- solved in 24:30
with t as (select id from Stadium 
where people >= 100)

select id2.id, s.visit_date, s.people
from (
select case
    when id in (select id from t) and (id+1) in (select id from t) and (id+2) in (select id from t) then id
    when id in (select id from t) and (id-1) in (select id from t) and (id-2) in (select id from t) then id 
    when id in (select id from t) and (id+1) in (select id from t) and (id-1) in (select id from t) then id 
    else 0 
    end as id 
from t
group by 1
) as id2
join Stadium s
on id2.id=s.id

-- others solution:
-- SELECT 
--     DISTINCT a.*
-- FROM 
--     stadium AS a, stadium AS b, stadium AS c
-- WHERE
--      a.people >= 100 AND b.people >= 100 AND c.people >= 100
-- AND 
--     (
--        (a.id - b.id = 1 AND b.id - c.id = 1)
--     OR (c.id - b.id = 1 AND b.id - a.id = 1)
--     OR (b.id - a.id = 1 AND a.id - c.id = 1)
--     )
-- ORDER BY visit_date

