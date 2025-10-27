-- solved in 11:54
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by 1
