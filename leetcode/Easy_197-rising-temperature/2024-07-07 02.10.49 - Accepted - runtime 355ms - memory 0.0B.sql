# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
JOIN Weather w2
ON w1.recordDate = DATE_ADD(w2.recordDate, Interval 1 Day)
WHERE w1.temperature > w2.temperature;