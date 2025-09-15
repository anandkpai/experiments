--
-- @lc app=leetcode id=586 lang=mysql
--
-- [586] Customer Placing the Largest Number of Orders
--

-- @lc code=start
# Write your MySQL query statement below
with 
custorders as 
(
    select 
        customer_number ,
        count(order_number) as OrderCount
    from Orders
    group by 
        customer_number
),
maxOrders as (Select max(OrderCount) as maxOrderCount from custorders)
select 
    c.customer_number 
from    
    custorders c
cross join 
    maxOrders m
where
    c.OrderCount = m.maxOrderCount

-- @lc code=end

