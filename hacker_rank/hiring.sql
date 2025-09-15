select 
    experience, 
    count(if(experience='Senior',1,null)) as senior_count, 
    sum(if(experience='Senior',salary,0)) as senior_budget,
    count(if(experience='Junior',1,null)) as junior_count, 
    sum(if(experience='Junior',salary,0)) as junior_budget
from
    (
        select 
            experience, 
            salary
        from 
            Candidates 
        order by 
            salary
    ) as salary_sorted_candidates
group by 
    experience
    having senior_budget < 20000