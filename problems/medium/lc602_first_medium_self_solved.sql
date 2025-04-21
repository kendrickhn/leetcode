'First Medium Self-solved'
'Monday April 21st 2025'
'Kendrick N'

SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
);
WITH Manager AS (
    SELECT DISTINCT managerId,
           COUNT(*) 
    FROM Employee
    GROUP BY 1 
    HAVING COUNT(*) >= 5
)
SELECT E.name 
FROM Employee E
JOIN Manager M 
  ON E.id = M.managerId;
