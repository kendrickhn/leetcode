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
