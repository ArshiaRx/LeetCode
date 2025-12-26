SELECT eu.unique_id as unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu using(id)

