--
-- @lc app=leetcode id=577 lang=mysql
--
-- [577] Employee Bonus
--

-- @lc code=start
# Write your MySQL query statement below
select 
    e.name, 
    b.Bonus
from 
    employee e
left outer join 
    bonus b 
on 
    e.empId = b.empId
where 
    b.bonus < 1000
    or b.bonus is Null 

-- @lc code=end

