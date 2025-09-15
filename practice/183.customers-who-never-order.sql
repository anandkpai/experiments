--
-- @lc app=leetcode id=183 lang=mysql
--
-- [183] Customers Who Never Order
--

-- @lc code=start
# Write your MySQL query statement below
select 
    c.name as Customers
    -- count(o.id) as orderCount 
from 
    Customers c 
left outer join Orders o 
    on c.id = o.customerId 
group by 
    c.id 
having 
    count(o.id) = 0 
-- @lc code=end

