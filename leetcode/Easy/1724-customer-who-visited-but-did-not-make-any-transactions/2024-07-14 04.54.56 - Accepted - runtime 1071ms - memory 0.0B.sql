# Write your MySQL query statement below
SELECT customer_id, COUNT(visit_id) as count_no_trans
From Visits v
WHERE NOT EXISTS (
    SELECT visit_id FROM Transactions t
    WHERE t.visit_id = v.visit_id

)

GROUP by customer_id
