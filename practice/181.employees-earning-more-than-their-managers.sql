--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below

select 
    e.name as Employee
from employee e
inner join employee m
on e.managerId = m.id 
where 
    e.salary > m.salary 

-- @lc code=end

