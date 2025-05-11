-- solved in 36:50
with list as 
(select student_id, subject, count(*) 
from Scores
group by 1,2
having count(*) >= 2) 

select fst.student_id, fst.subject, fst.first_score, lts.latest_score
from
(select s.student_id,s.subject,s.score as first_score
from Scores s
join 
(select student_id, subject, min(exam_date) as exam_date
from Scores
where student_id in (select student_id from list)
group by student_id, subject ) f
on s.student_id = f.student_id and s.subject=f.subject and s.exam_date = f.exam_date) fst
join
(select s.student_id,s.subject,s.score as latest_score
from Scores s
join 
(select student_id, subject, max(exam_date) as exam_date
from Scores
where student_id in (select student_id from list)
group by student_id, subject) l
on s.student_id = l.student_id and s.subject=l.subject and s.exam_date = l.exam_date) lts
on fst.student_id = lts.student_id and fst.subject=lts.subject

where lts.latest_score > fst.first_score
order by 1,2

-- solution:
-- WITH Ranked AS (
--     SELECT
--     student_id,
--     subject,
--     FIRST_VALUE(score) OVER(PARTITION BY student_id,subject ORDER BY exam_date) AS first_score,
--     FIRST_VALUE(score) OVER(PARTITION BY student_id,subject ORDER BY exam_date DESC) AS latest_score
--     FROM Scores
-- )
-- SELECT DISTINCT * FROM Ranked
-- WHERE first_score<latest_score
-- ORDER BY student_id,subject