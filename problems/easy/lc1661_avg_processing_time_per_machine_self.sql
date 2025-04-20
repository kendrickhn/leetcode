-- LeetCode Problem: 1661. Average Time of Process per Machine
-- Solved by: self
-- Date: 2025-04-13

-- ✅ Solution using JOIN
SELECT 
    s.machine_id, 
    ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
FROM Activity s
JOIN Activity e 
  ON s.machine_id = e.machine_id 
 AND s.process_id = e.process_id
WHERE s.activity_type = 'start' AND e.activity_type = 'end'
GROUP BY s.machine_id;

-- ✅ Solution using window function (LEAD)
SELECT 
    machine_id, 
    ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM (
    SELECT 
        machine_id,
        process_id,
        timestamp AS start_time,
        LEAD(timestamp) OVER (PARTITION BY machine_id, process_id ORDER BY timestamp) AS end_time
    FROM Activity
    WHERE activity_type = 'start'
    UNION ALL
    SELECT 
        machine_id,
        process_id,
        NULL AS start_time,
        timestamp AS end_time
    FROM Activity
    WHERE activity_type = 'end'
) t
WHERE start_time IS NOT NULL AND end_time IS NOT NULL
GROUP BY machine_id;
