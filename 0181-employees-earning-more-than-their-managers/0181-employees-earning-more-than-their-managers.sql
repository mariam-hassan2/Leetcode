# Write your MySQL query statement below


SELECT a.name as "Employee"
from Employee as a, Employee as b
where a.managerId = b.Id
and a.salary > b.salary