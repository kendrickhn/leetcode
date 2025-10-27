-- solved in 50:04
-- mine
-- select visited_on, 
--     sum(amount) over (order by visited_on
--   rows between 6 preceding and 0 following) as 'amount',
--     round((avg(amount) over (order by visited_on
--   rows between 6 preceding and 0 following)),2) as 'average_amount'
-- from (
--     select visited_on, 
--     sum(amount) as amount
--     from Customer
--     group by 1
-- ) t
-- where visited_on
--     >= date_add((select min(visited_on) from Customer), INTERVAL 6 DAY)

-- ai's
WITH daily AS (
  SELECT
    visited_on,
    SUM(amount) AS amount
  FROM Customer
  GROUP BY visited_on
)

SELECT
  d1.visited_on,
  (
    SELECT SUM(d2.amount)
    FROM daily d2
    WHERE d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY)
                           AND d1.visited_on
  ) AS amount,
  ROUND(
    (
      SELECT AVG(d3.amount)
      FROM daily d3
      WHERE d3.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY)
                             AND d1.visited_on
    ),
    2
  ) AS average_amount
FROM daily d1
WHERE d1.visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM daily), INTERVAL 6 DAY)
ORDER BY d1.visited_on;
