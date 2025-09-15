import pandas as pd

employee = pd.DataFrame(columns=['id','salary'], data = [(1,100),(2,200),(3,300)])

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary_sorted = employee.salary.sort_values(ascending=False).drop_duplicates()    
    nth_salary = salary_sorted.iat[N] if salary_sorted.size > N else None 
    return pd.DataFrame(columns=[f'getNthHighestSalary({N})'], data=[nth_salary])

    


s = nth_highest_salary(employee,3)

print(s.isna())