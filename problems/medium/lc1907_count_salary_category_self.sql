-- solved by others

-- Understanding SQL's Execution Order:
-- When SQL runs a query, it processes it in a specific order:

-- FROM – where it grabs the data from the table.
-- JOIN – if you're combining tables.
-- WHERE – filtering rows.
-- GROUP BY – grouping the filtered rows.
-- HAVING – filtering groups after grouping.
-- SELECT – choosing the columns to return.

-- Why It’s Tricky:
-- Here’s the problem: when you tell SQL to group the data by salary categories (Low Salary, Average Salary, High Salary), it only groups rows that actually match the conditions.

-- It first pulls the data from the accounts table.
-- It then groups only the accounts that fit those conditions (Low or High Salary in this case).
-- But if no accounts have an income between 20,000and50,000, there will be no "Average Salary" group to return.
-- So, even though you’ve defined Average Salary, SQL won’t include it because there’s no data that matches.

SELECT "Low Salary" as category, sum(income<20000) AS accounts_count FROM Accounts
union
SELECT "Average Salary" as category, sum(income>=20000 and income<=50000) AS accounts_count FROM Accounts
union
SELECT "High Salary" as category, sum(income>50000) AS accounts_count FROM Accounts