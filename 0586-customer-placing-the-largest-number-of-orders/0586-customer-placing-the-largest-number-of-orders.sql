# Write your MySQL query statement below


select customer_number
from Orders
group by customer_number
order by Count(*) desc limit 1