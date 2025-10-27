-- Solved in 60:00 
with greatest_user as 
(select mr.user_id, u.name 
from MovieRating mr  
join Users u 
on u.user_id=mr.user_id 
group by mr.user_id 
order by count(*) desc, u.name asc
limit 1),

greatest_movie as (select mr.movie_id, m.title
from MovieRating mr
join Movies m 
on m.movie_id=mr.movie_id 
where DATE_FORMAT(mr.created_at, '%Y-%m')='2020-02'
group by mr.movie_id
order by avg(rating) desc, title asc
limit 1)

select name as results from greatest_user
union all 
select title as results from greatest_movie

