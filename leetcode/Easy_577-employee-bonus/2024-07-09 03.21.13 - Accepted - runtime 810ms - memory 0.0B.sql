# Write your MySQL query statement below
SELECT e.name, Bonus.bonus
FROM Employee e
LEFT JOIN Bonus
ON e.empID = Bonus.empID
WHERE bonus < 1000 OR Bonus is NULL;